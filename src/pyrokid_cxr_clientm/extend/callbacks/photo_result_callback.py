from ...utils import ValueUtil

class PhotoResultCallback:
	"""PhotoResultCallback Interface - Please extend this class and implement the methods"""
	def onPhotoResult(self, paramCxrStatus: ValueUtil.CxrStatus, paramArrayOfbyte: bytes) -> None: pass
