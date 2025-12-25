from ...utils import ValueUtil

class UnsyncNumResultCallback:
	"""UnsyncNumResultCallback Interface - Please extend this class and implement the methods"""
	def onUnsyncNumResult(self, status: ValueUtil.CxrStatus, audioNum: int, pictureNum: int, videoNum: int) -> None: pass
