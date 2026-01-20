"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/GlassInfoResultCallback.java in Python"""

from abc import ABC, abstractmethod
from ..infos import GlassInfo
from ...utils import ValueUtil

class GlassInfoResultCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.GlassInfoResultCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onGlassInfoResult(self, status: ValueUtil.CxrStatus, glassInfo: GlassInfo) -> None: pass
