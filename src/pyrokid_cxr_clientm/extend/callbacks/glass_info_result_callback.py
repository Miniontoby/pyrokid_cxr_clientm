from ..infos import GlassInfo
from ...utils import ValueUtil

class GlassInfoResultCallback:
	"""GlassInfoResultCallback Interface - Please extend this class and implement the methods"""
	def onGlassInfoResult(self, status: ValueUtil.CxrStatus, glassesInfo: GlassInfo) -> None: pass
