"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/GlassVersionCallback.java in Python"""

from abc import ABC, abstractmethod

class GlassVersionCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.GlassVersionCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onGlassVersion(self, success: bool, version: str) -> None: pass
