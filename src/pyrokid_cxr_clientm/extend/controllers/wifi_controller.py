"""com.rokid.cxr.client-m:1.0.4 - extend/controllers/WifiController.java in Python

WifiController class gets the IP address of the glasses based on open ports
The original Android code actually did Wifi Direct/P2P connections, but I cannot do that.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from json import dumps as json_dumps
from threading import Thread
from time import sleep
import socket, struct, platform, subprocess, re
import concurrent.futures
from typing import Optional, List

from ...libcaps import Caps
from ...utils import LogUtil, ValueUtil
#from ...controllers.cxr_controller import CxrController

def get_local_subnet() -> tuple[str, int]:
	"""Get local subnet and calculate number of hosts"""
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		local_ip = s.getsockname()[0]
		s.close()
		
		system = platform.system()
		netmask = None
		
		if system == 'Windows':
			startupinfo = subprocess.STARTUPINFO()
			startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
			startupinfo.wShowWindow = subprocess.SW_HIDE
			
			result = subprocess.run(['ipconfig'], capture_output=True, text=True,
				startupinfo=startupinfo,
				creationflags=subprocess.CREATE_NO_WINDOW)
			
			lines = result.stdout.split('\n')
			for i, line in enumerate(lines):
				if local_ip in line:
					# Look for subnet mask in next few lines
					for j in range(i, min(i+10, len(lines))):
						if 'Subnet Mask' in lines[j]:
							mask_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', lines[j])
							if mask_match:
								netmask = mask_match.group(1)
								break
					break
		
		elif system == 'Linux':
			# Try ip command first (modern)
			try:
				result = subprocess.run(['ip', 'addr', 'show'], 
					capture_output=True, text=True, timeout=5)
				
				lines = result.stdout.split('\n')
				for line in lines:
					if local_ip in line and 'inet ' in line:
						# Format: "inet 192.168.1.100/24 brd ..."
						match = re.search(rf'inet {re.escape(local_ip)}/(\d+)', line)
						if match:
							cidr = int(match.group(1))
							# Convert CIDR to netmask
							mask_int = (0xffffffff << (32 - cidr)) & 0xffffffff
							netmask = socket.inet_ntoa(struct.pack('>I', mask_int))
							break
			except:
				pass
			
			# Fallback to ifconfig
			if not netmask:
				try:
					result = subprocess.run(['ifconfig'], 
						capture_output=True, text=True, timeout=5)
					
					lines = result.stdout.split('\n')
					for i, line in enumerate(lines):
						if local_ip in line:
							# Look for netmask in same or next line
							for j in range(i, min(i+3, len(lines))):
								mask_match = re.search(r'netmask\s+(\d+\.\d+\.\d+\.\d+)', lines[j])
								if not mask_match:
									# Try hex format: netmask 0xffffff00
									hex_match = re.search(r'netmask\s+(0x[0-9a-fA-F]+)', lines[j])
									if hex_match:
										mask_int = int(hex_match.group(1), 16)
										netmask = socket.inet_ntoa(struct.pack('>I', mask_int))
										break
								else:
									netmask = mask_match.group(1)
									break
							break
				except:
					pass
		
		elif system == 'Darwin':  # macOS
			try:
				result = subprocess.run(['ifconfig'], 
					capture_output=True, text=True, timeout=5)
				
				lines = result.stdout.split('\n')
				for i, line in enumerate(lines):
					if local_ip in line and 'inet ' in line:
						# Format: "inet 192.168.1.100 netmask 0xffffff00"
						for j in range(i, min(i+3, len(lines))):
							# Look for hex netmask
							hex_match = re.search(r'netmask\s+(0x[0-9a-fA-F]+)', lines[j])
							if hex_match:
								mask_int = int(hex_match.group(1), 16)
								netmask = socket.inet_ntoa(struct.pack('>I', mask_int))
								break
							# Or decimal format
							mask_match = re.search(r'netmask\s+(\d+\.\d+\.\d+\.\d+)', lines[j])
							if mask_match:
								netmask = mask_match.group(1)
								break
						break
			except:
				pass
		
		# If we got a netmask, calculate CIDR and return
		if netmask:
			cidr = sum([bin(int(x)).count('1') for x in netmask.split('.')])
			num_hosts = 2**(32 - cidr) - 2
			if num_hosts == -1: num_hosts = 1
			
			# Calculate network address
			ip_int = struct.unpack('>I', socket.inet_aton(local_ip))[0]
			mask_int = struct.unpack('>I', socket.inet_aton(netmask))[0]
			network_int = ip_int & mask_int
			network = socket.inet_ntoa(struct.pack('>I', network_int))
			
			return f"{network}/{cidr}", num_hosts
		
		# Default fallback to /24
		base = '.'.join(local_ip.split('.')[0:3])
		return f"{base}.0/24", 254
		
	except Exception as e:
		print(f"Error getting subnet: {e}")
		return "192.168.1.0/24", 254

def get_and_parse_subnet() -> tuple[str, str, int]:
	"""Get the local subnet and parse subnet CIDR notation and return base IP, start IP, and count"""
	subnet, num_hosts = get_local_subnet()

	ip_part, cidr = subnet.split('/')
	cidr = int(cidr)
	
	# Convert IP to integer
	ip_int = struct.unpack('>I', socket.inet_aton(ip_part))[0]
	
	# Calculate network address
	mask = (0xffffffff << (32 - cidr)) & 0xffffffff
	network = ip_int & mask
	
	# First usable IP (network + 1)
	first_ip_int = network + 1
	first_ip = socket.inet_ntoa(struct.pack('>I', first_ip_int))
	
	# Base for iteration (network address)
	base_ip = socket.inet_ntoa(struct.pack('>I', network))
	
	return base_ip, first_ip, num_hosts

def scan_port_manual(port: int, timeout: float = 0.5) -> List[str]:
	"""Manually scan subnet for open port"""
	
	# Parse subnet to get actual IP range
	base_ip, first_ip, num_hosts = get_and_parse_subnet()
	
	# Get base as integer for iteration
	base_int = struct.unpack('>I', socket.inet_aton(base_ip))[0]
	
	def check_port(ip_int: int) -> Optional[str]:
		try:
			ip = socket.inet_ntoa(struct.pack('>I', ip_int))
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(timeout)
			result = sock.connect_ex((ip, port))
			sock.close()
			
			if result == 0: return ip
		except:
			pass
		return None
	
	ips = []
	
	# Scan all IPs in parallel
	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		futures = []
		# Start from network + 1, end at network + num_hosts
		for i in range(1, num_hosts + 1):
			ip_int = base_int + i
			futures.append(executor.submit(check_port, ip_int))
		
		for future in concurrent.futures.as_completed(futures):
			result = future.result()
			if result: ips.append(result)
	
	return ips

def find_device_by_port(port: int = 8848) -> Optional[str]:
	"""Find device with specific port open"""

	ips = scan_port_manual(port)

	if ips: return ips[0]
	return None

class WifiController:
	"""com.rokid.cxr.client.extend.controller.WifiController Java class to Python"""
	a = None # Context
	"""mContext"""
	b: ValueUtil.CxrStatus = None
	"""mWifiStatus"""
	c: WifiController.Callback = None
	"""mCallback"""
	d: str = None
	"""mDeviceName"""
	n: int = 0
	"""mRetryCount"""
	o: bool = False
	"""mIsConnected"""

	class Callback(ABC):
		"""WifiController.Callback Interface - Please extend this class and implement the methods"""
		@abstractmethod
		def onStatusUpdate(self, cxrStatus: ValueUtil.CxrStatus, cxrWifiErrorCode: ValueUtil.CxrWifiErrorCode) -> None: pass
		@abstractmethod
		def onAddress(self, address: str) -> None: pass

	def __init__(self):
		LogUtil.i("WifiController", "WifiController constructed")

	@staticmethod
	def getInstance() -> WifiController:
		LogUtil.v("WifiController", "getInstance")
		return _f.a

	def init(self, context, deviceName: str, callback: WifiController.Callback):
		LogUtil.i("WifiController", "init")
		try:
			self.b = ValueUtil.CxrStatus.WIFI_INIT
			self.c = None
			self.deinit(ValueUtil.CxrWifiErrorCode.SUCCEED)
			self.a = context
			self.d = deviceName
			self.c = callback
			self.connectP2pService()
		except Exception as exception:
			LogUtil.e("WifiController", exception)

	def isConnected(self) -> bool:
		LogUtil.d("WifiController", "isConnected")
		return self.o

	def deinit(self, cxrWifiErrorCode: ValueUtil.CxrWifiErrorCode) -> ValueUtil.CxrStatus:
		LogUtil.i("WifiController", "deinit")
		cxrStatus = ValueUtil.CxrStatus.REQUEST_FAILED
		try:
			if self.c is not None:
				LogUtil.i("WifiController", "notify glass to close wifi p2p")
				strValue = json_dumps({
					"type": "Android"
				})
				LogUtil.i("WifiController", "typeJson: %s", strValue)
				caps = Caps()
				caps.write("Sync_Stop")
				caps.write(strValue)
				#cxrStatus = self.CxrController.getInstance().request(1, "Med", caps, None)
			else:
				LogUtil.e("WifiController", "mCallback is null")
			self.d = None
			self.n = 0
			self.o = False
			self.updateStatus(ValueUtil.CxrStatus.WIFI_UNAVAILABLE, cxrWifiErrorCode)
			self.c = None
		except Exception as exception:
			LogUtil.e("WifiController", exception)
		return cxrStatus

	def updateStatus(self, cxrStatus: ValueUtil.CxrStatus, cxrWifiErrorCode: ValueUtil.CxrWifiErrorCode) -> None:
		LogUtil.i("WifiController", "updateStatus: %s, errorCode: %s", cxrStatus, cxrWifiErrorCode)
		callback: WifiController.Callback = self.c
		if callback is None:
			LogUtil.e("WifiController", "mCallback is null")
		else:
			if self.b == cxrStatus:
				LogUtil.e("WifiController", "mWifiStatus == status")
				return
			self.b = cxrStatus
			self.o = (cxrStatus == ValueUtil.CxrStatus.WIFI_AVAILABLE)
			callback.onStatusUpdate(cxrStatus, cxrWifiErrorCode)

	def connectToDevice(self) -> None:
		LogUtil.i("WifiController", "connectToDevice")
		hostAddress = find_device_by_port(port=8848)
		if hostAddress:
			callback: WifiController.Callback = self.c
			if callback is not None:
				callback.onAddress(hostAddress)
			else:
				LogUtil.e("WifiController", "mCallback is null")
			self.updateStatus(ValueUtil.CxrStatus.WIFI_AVAILABLE, ValueUtil.CxrWifiErrorCode.SUCCEED)
			return

		i = self.n
		if self.n < 3:
			self.n = i + 1
			sleep(1)
			self.connectToDevice()
		else:
			LogUtil.e("WifiController", "mRetryCount == WIFI_MAX_RETRY_COUNT")
			self.deinit(ValueUtil.CxrWifiErrorCode.WIFI_CONNECT_FAILED)

	def connectP2pService(self) -> None:
		LogUtil.i("WifiController", "connectP2pService")
		self.n = 0
		Thread(target=self.connectToDevice, daemon=True).start()

class _f: a: WifiController = WifiController()

__all__ = ['WifiController']
