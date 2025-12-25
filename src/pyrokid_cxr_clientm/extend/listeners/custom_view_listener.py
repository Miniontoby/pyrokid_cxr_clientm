class CustomViewListener:
	"""CustomViewListener Interface - Please extend this class and implement the methods"""
	def onIconsSent(self) -> None: pass
	def onOpened(self) -> None: pass
	def onOpenFailed(self, errorCode: int) -> None: pass
	def onUpdated(self) -> None: pass
	def onClosed(self) -> None: pass
