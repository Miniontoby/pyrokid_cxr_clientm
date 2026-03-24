"""com.rokid.cxr.client-m:1.0.9 - extend/callbacks/GlassInfoResultCallback.java in Python"""

from abc import ABC, abstractmethod
from ..infos import GlassInfo
from ...utils import ValueUtil

class GlassInfoResultCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.GlassInfoResultCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onGlassInfoResult(self, cxrStatus: ValueUtil.CxrStatus, glassInfo: GlassInfo) -> None: pass
