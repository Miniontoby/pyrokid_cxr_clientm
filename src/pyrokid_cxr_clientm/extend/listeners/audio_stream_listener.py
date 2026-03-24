"""com.rokid.cxr.client-m:1.0.9 - extend/listeners/AudioStreamListener.java in Python"""

from abc import ABC, abstractmethod

class AudioStreamListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.AudioStreamListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onStartAudioStream(self, i: int, codec: int, cmd: str) -> None: pass
	@abstractmethod
	def onAudioStream(self, i: int, bArr: bytearray, offset: int, size: int) -> None: pass
	@abstractmethod
	def onAudioStreamFinish(self, i: int) -> None: pass
