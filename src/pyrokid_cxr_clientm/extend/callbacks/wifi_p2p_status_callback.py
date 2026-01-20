"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/WifiP2PStatusCallback.java in Python"""

from abc import ABC, abstractmethod
from ...utils import ValueUtil

class WifiP2PStatusCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.WifiP2PStatusCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onConnected(self) -> None: pass
	@abstractmethod
	def onDisconnected(self) -> None: pass
	@abstractmethod
	def onFailed(self, errorCode: ValueUtil.CxrWifiErrorCode) -> None: pass
