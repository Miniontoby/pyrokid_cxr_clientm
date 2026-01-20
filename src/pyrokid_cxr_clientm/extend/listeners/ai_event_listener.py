"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/AiEventListener.java in Python"""

from abc import ABC, abstractmethod

class AiEventListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.AiEventListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onAiKeyDown(self) -> None: pass
	@abstractmethod
	def onAiBothKeyDown(self) -> None: pass # Added by me
	@abstractmethod
	def onAiKeyUp(self) -> None: pass
	@abstractmethod
	def onAiExit(self) -> None: pass
