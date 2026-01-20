"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/MediaFilesUpdateListener.java in Python"""

from abc import ABC, abstractmethod

class MediaFilesUpdateListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.MediaFilesUpdateListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onMediaFilesUpdated(self) -> None: pass
