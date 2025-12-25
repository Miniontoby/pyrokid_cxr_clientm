class GlassVersionCallback:
	"""GlassVersionCallback Interface - Please extend this class and implement the methods"""
	def onGlassVersion(self, success: bool, version: str) -> None: pass
