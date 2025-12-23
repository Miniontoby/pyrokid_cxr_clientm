from ...utils import ValueUtil

class PhotoPathCallback:
	"""PhotoPathCallback Interface - Please extend this class and implement the methods"""
	def onPhotoPath(self, paramCxrStatus: ValueUtil.CxrStatus, paramString: str) -> None: pass
