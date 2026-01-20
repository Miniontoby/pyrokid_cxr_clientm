"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/WifiListCallback.java in Python"""

from abc import ABC, abstractmethod
from ...utils import ValueUtil
from ..infos import RKWifiInfo

class WifiListCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.WifiListCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onWifiList(self, status: ValueUtil.CxrStatus, wifiList: list[RKWifiInfo]) -> None: pass
