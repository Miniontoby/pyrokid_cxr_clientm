from __future__ import annotations
from .utils import ValueUtil
from .libcaps import Caps
from enum import IntEnum

class PacketTypeIds(IntEnum):
	"""Packet Type IDs used in :class:`CXRSocketProtocol` Requests and Responses"""
	REQUEST = 0x1001 # request
	RESPONSE = 0x1002 # response

	NOTIFY = 0x1003 # notify

	AUTH_REQUEST = 0x1004 # authRequest
	AUTH_RESPONSE = 0x1005 # authResponse
	ROKID_ACCOUNT_REQUEST = 0x1006 # changeRokidAccount

	# These I don't know yet.
	TRANSFER_INFO = 0x2001
	TRANSFER_INFO_TWO = 0x2002
	TRANSFER_INFO_THREE = 0x2003

	# I am NOT sure about these values!
	AI_START = 0x3001
	AI_DATA = 0x3002
	AI_END = 0x3003

class CXRSocketProtocol:
	a: str
	b = None # BluetoothSocket
	c = None # InputStream
	d = None # OutputStream
	e = None # Runnable
	f: int = 0
	g: bool = False
	h: bool = False
	i: CXRSocketProtocol.Callback = None
	j: int

	def version(self) -> int: return 4

	class Callback:
		"""Callback Interface - Please extend the class and write your own methods!"""
		def onResponse(self, param1Int: int, param1Caps: Caps) -> None: pass
    
		def onNotify(self, param1String: str, param1Caps: Caps) -> None: pass
    
		def onReceived(self, param1String: str, param1Caps: Caps, param1ArrayOfbyte: bytes) -> None: pass
    
		def onStartAudioStream(self, param1Int: int, param1String: str, param1Caps: Caps) -> None: pass
    
		def onAudioStream(self, param1ArrayOfbyte: bytes, param1Int1: int, param1Int2: int) -> None: pass
    
		def onARTCFrame(self, param1ArrayOfbyte: bytes) -> None: pass
    
		def onDisconnect(self) -> None: pass
