"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/CustomViewListener.java in Python"""

from abc import ABC, abstractmethod

class CustomViewListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.CustomViewListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onIconsSent(self) -> None: pass
	@abstractmethod
	def onOpened(self) -> None: pass
	@abstractmethod
	def onOpenFailed(self, errorCode: int) -> None: pass
	@abstractmethod
	def onUpdated(self) -> None: pass
	@abstractmethod
	def onClosed(self) -> None: pass
