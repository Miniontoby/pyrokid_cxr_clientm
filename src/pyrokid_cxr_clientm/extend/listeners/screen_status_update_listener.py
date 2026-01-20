"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/ScreenStatusUpdateListener.java in Python"""

from abc import ABC, abstractmethod

class ScreenStatusUpdateListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.ScreenStatusUpdateListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onScreenStatusUpdated(self, screenOn: bool) -> None: pass
