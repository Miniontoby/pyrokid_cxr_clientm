"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/UnsyncNumResultCallback.java in Python"""

from abc import ABC, abstractmethod
from ...utils import ValueUtil

class UnsyncNumResultCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.UnsyncNumResultCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onUnsyncNumResult(self, status: ValueUtil.CxrStatus, audioNum: int, pictureNum: int, videoNum: int) -> None: pass
