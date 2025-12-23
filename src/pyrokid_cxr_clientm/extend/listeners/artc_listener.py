class ArtcListener:
	"""ArtcListener Interface - Please extend this class and implement the methods"""
	def onArtcStart(self) -> None: pass
	def onArtcStop(self) -> None: pass
	def onArtsFrame(self, paramArrayOfbyte: bytes) -> None: pass
