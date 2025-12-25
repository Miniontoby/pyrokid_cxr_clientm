from ...utils import ValueUtil

class SendStatusCallback:
	"""SendStatusCallback Interface - Please extend this class and implement the methods"""
	def onSendSucceed(self) -> None: pass
	def onSendFailed(self, errorCode: ValueUtil.CxrSendErrorCode) -> None: pass
