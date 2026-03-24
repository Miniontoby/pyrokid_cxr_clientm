"""com.rokid.cxr.client-m:1.0.9 - extend/callbacks/WifiHotStatusCallback.java in Python"""

from abc import ABC, abstractmethod

class WifiHotStatusCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.WifiHotStatusCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onWifiHotAvailable(self, account: str, password: str, ip: str, securityType: int) -> None: pass
