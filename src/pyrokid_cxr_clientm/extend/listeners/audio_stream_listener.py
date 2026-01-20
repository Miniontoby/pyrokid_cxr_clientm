"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/AudioStreamListener.java in Python"""

from abc import ABC, abstractmethod

class AudioStreamListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.AudioStreamListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onStartAudioStream(self, codec: int, cmd: str) -> None: pass
	@abstractmethod
	def onAudioStream(self, paramArrayOfbyte: bytes, paramInt1: int, size: int) -> None: pass
