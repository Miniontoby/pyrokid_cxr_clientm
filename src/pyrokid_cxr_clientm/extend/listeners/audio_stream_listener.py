class AudioStreamListener:
	"""AudioStreamListener Interface - Please extend this class and implement the methods"""
	def onStartAudioStream(self, paramInt: int, paramString: str) -> None: pass
	def onAudioStream(self, paramArrayOfbyte: bytes, paramInt1: int, paramInt2: int) -> None: pass
