"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/BrightnessUpdateListener.java in Python"""

from abc import ABC, abstractmethod

class BrightnessUpdateListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.BrightnessUpdateListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onBrightnessUpdated(self, brightness: int) -> None: pass
