"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/AudioSceneIdCallback.java in Python"""

from abc import ABC, abstractmethod

class AudioSceneIdCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.AudioSceneIdCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onAudioSceneId(self, audioSceneId: int, success: bool) -> None: pass
