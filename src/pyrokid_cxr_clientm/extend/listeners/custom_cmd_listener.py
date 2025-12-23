from ...libcaps import Caps

class CustomCmdListener:
	"""CustomCmdListener Interface - Please extend this class and implement the methods"""
	def onCustomCmd(self, cmd: str, args: Caps) -> None: pass
