from ...utils import ValueUtil

class BluetoothStatusCallback:
	"""BluetoothStatusCallback Interface - Please extend this class and implement the methods"""
	def onConnectionInfo(self, socketUuid: str, macAddress: str, rokidAccount: str, glassesType: int) -> None: pass
	def onConnected(self) -> None: pass
	def onDisconnected(self) -> None: pass
	def onFailed(self, errorCode: ValueUtil.CxrBluetoothErrorCode) -> None: pass
