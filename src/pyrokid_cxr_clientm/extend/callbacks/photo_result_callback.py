from ...utils import ValueUtil

class PhotoResultCallback:
	"""PhotoResultCallback Interface - Please extend this class and implement the methods"""
	def onPhotoResult(self, status: ValueUtil.CxrStatus, photo: bytearray) -> None:
		"""
		:param ValueUtil.CxrStatus status: Photo take status
		:param bytes photo: WebP photo data bytearray
		"""
		pass
