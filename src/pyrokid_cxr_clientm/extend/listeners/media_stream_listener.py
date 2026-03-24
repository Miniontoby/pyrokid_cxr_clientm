"""com.rokid.cxr.client-m:1.0.9 - extend/listeners/MediaStreamListener.java in Python"""

from abc import ABC, abstractmethod

class MediaStreamListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.MediaStreamListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onCameraOpened(self) -> None: pass
	@abstractmethod
	def onCameraClosed(self) -> None: pass
	@abstractmethod
	def onCameraError(self) -> None: pass
	@abstractmethod
	def onCameraFrame(self, bArr: bytearray, j: int) -> None: pass
