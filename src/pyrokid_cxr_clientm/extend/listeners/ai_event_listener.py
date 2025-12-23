class AiEventListener:
	"""AiEventListener Interface - Please extend this class and implement the methods"""
	def onAiKeyDown(self) -> None: pass
	def onAiBothKeyDown(self) -> None: pass # Added by me
	def onAiKeyUp(self) -> None: pass
	def onAiExit(self) -> None: pass
