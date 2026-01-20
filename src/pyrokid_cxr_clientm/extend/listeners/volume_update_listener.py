"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/VolumeUpdateListener.java in Python"""

from abc import ABC, abstractmethod

class VolumeUpdateListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.VolumeUpdateListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onVolumeUpdated(self, volume: int) -> None: pass
