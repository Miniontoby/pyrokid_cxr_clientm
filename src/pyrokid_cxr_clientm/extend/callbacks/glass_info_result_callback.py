from ..infos import GlassInfo
from ...utils import ValueUtil

class GlassInfoResultCallback:
	"""GlassInfoResultCallback Interface - Please extend this class and implement the methods"""
	def onGlassInfoResult(self, paramCxrStatus: ValueUtil.CxrStatus, paramGlassInfo: GlassInfo) -> None: pass
