"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/PhotoResultCallback.java in Python"""

from abc import ABC, abstractmethod
from ...utils import ValueUtil

class PhotoResultCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.PhotoResultCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onPhotoResult(self, status: ValueUtil.CxrStatus, photo: bytearray) -> None:
		"""
		:param ValueUtil.CxrStatus status: Photo take status
		:param bytes photo: WebP photo data bytearray
		"""
		pass
