"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/ArtcListener.java in Python"""

from abc import ABC, abstractmethod

class ArtcListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.ArtcListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onArtcStart(self) -> None: pass
	@abstractmethod
	def onArtcStop(self) -> None: pass
	@abstractmethod
	def onArtcFrame(self, data: bytes) -> None: pass
