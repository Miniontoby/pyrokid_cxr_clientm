"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/BluetoothStatusCallback.java in Python"""

from abc import ABC, abstractmethod
from ...utils import ValueUtil

class BluetoothStatusCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.BluetoothStatusCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onConnectionInfo(self, socketUuid: str, macAddress: str, rokidAccount: str, glassesType: int) -> None: pass
	@abstractmethod
	def onConnected(self) -> None: pass
	@abstractmethod
	def onDisconnected(self) -> None: pass
	@abstractmethod
	def onFailed(self, errorCode: ValueUtil.CxrBluetoothErrorCode) -> None: pass
