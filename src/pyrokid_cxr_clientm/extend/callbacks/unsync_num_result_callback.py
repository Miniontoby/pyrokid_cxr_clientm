from ...utils import ValueUtil

class UnsyncNumResultCallback:
	"""UnsyncNumResultCallback Interface - Please extend this class and implement the methods"""
	def onUnsyncNumResult(self, paramCxrStatus: ValueUtil.CxrStatus, paramInt1: int, paramInt2: int, paramInt3: int) -> None: pass
