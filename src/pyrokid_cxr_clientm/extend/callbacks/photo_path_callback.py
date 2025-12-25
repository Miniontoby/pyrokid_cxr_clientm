from ...utils import ValueUtil

class PhotoPathCallback:
	"""PhotoPathCallback Interface - Please extend this class and implement the methods"""
	def onPhotoPath(self, status: ValueUtil.CxrStatus, path: str) -> None: pass
