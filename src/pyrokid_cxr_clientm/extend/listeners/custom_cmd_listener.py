"""com.rokid.cxr.client-m:1.0.9 - extend/listeners/CustomCmdListener.java in Python"""

from abc import ABC, abstractmethod
from ...libcaps import Caps

class CustomCmdListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.CustomCmdListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onCustomCmd(self, cmd: str, caps: Caps) -> None: pass
