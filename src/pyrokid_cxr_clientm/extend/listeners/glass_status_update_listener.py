"""com.rokid.cxr.client-m:1.0.9 - extend/listeners/GlassStatusUpdateListener.java in Python"""

from abc import ABC, abstractmethod

class GlassStatusUpdateListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.GlassStatusUpdateListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onWearingStatusUpdated(self, string: str) -> None: pass
	@abstractmethod
	def onGlassTempleStatusUpdated(self, string: str) -> None: pass
	@abstractmethod
	def onGlassGlobalTtsStatusUpdated(self, string: str) -> None: pass
