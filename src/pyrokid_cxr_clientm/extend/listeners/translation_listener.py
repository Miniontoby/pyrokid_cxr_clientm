"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/TranslationListener.java in Python"""

from abc import ABC, abstractmethod

class TranslationListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.TranslationListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onTranslationStart(self) -> None: pass
	@abstractmethod
	def onTranslationStop(self) -> None: pass
