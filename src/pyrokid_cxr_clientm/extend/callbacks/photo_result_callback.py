from ...utils import ValueUtil

class PhotoResultCallback:
	"""PhotoResultCallback Interface - Please extend this class and implement the methods"""
	def onPhotoResult(self, status: ValueUtil.CxrStatus, photo: bytes) -> None: pass
