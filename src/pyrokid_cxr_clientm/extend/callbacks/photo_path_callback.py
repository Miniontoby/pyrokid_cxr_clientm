"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/PhotoPathCallback.java in Python"""

from abc import ABC, abstractmethod
from ...utils import ValueUtil

class PhotoPathCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.PhotoPathCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onPhotoPath(self, status: ValueUtil.CxrStatus, photoPath: str) -> None: pass
