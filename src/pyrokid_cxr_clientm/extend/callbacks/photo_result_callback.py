"""com.rokid.cxr.client-m:1.0.9 - extend/callbacks/PhotoResultCallback.java in Python"""

from abc import ABC, abstractmethod
from ...utils import ValueUtil

class PhotoResultCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.PhotoResultCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onPhotoResult(self, cxrStatus: ValueUtil.CxrStatus, bArr: bytearray) -> None:
		"""
		:param ValueUtil.CxrStatus cxrStatus: Photo take status
		:param bytearray bArr: WebP photo data bytearray
		"""
		pass
