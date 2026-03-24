"""com.rokid.cxr.client-m:1.0.9 - extend/callbacks/PeriphDeviceCallback.java in Python"""

from abc import ABC, abstractmethod
from ..infos import BluetoothPeriphInfo
from ...utils import ValueUtil

class PeriphDeviceCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.PeriphDeviceCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onBluetoothPeriphList(self, cxrStatus: ValueUtil.CxrStatus, data: list[BluetoothPeriphInfo]) -> None: pass
