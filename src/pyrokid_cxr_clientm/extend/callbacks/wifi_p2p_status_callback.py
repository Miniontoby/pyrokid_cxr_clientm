from ...utils import ValueUtil

class WifiP2PStatusCallback:
	"""WifiP2PStatusCallback Interface - Please extend this class and implement the methods"""
	def onConnected(self) -> None: pass
	def onDisconnected(self) -> None: pass
	def onSendFailed(self, errorCode: ValueUtil.CxrWifiErrorCode) -> None: pass
