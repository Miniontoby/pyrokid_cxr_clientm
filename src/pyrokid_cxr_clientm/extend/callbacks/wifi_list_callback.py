from ..infos import RKWifiInfo
from ...utils import ValueUtil

class WifiListCallback:
	"""WifiListCallback Interface - Please extend this class and implement the methods"""
	def onWifiList(self, paramCxrStatus: ValueUtil.CxrStatus, paramList: list[RKWifiInfo]) -> None: pass
