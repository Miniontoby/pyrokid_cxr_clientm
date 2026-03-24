"""com.rokid.cxr.client-m:1.0.9 - extend/callbacks/WifiListCallback.java in Python"""

from abc import ABC, abstractmethod
from ..infos import RKWifiInfo
from ...utils import ValueUtil

class WifiListCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.WifiListCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onWifiList(self, cxrStatus: ValueUtil.CxrStatus, data: list[RKWifiInfo]) -> None: pass
