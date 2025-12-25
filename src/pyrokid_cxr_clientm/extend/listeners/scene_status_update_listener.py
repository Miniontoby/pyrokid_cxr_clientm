from ..infos import SceneStatusInfo

class SceneStatusUpdateListener:
	"""SceneStatusUpdateListener Interface - Please extend this class and implement the methods"""
	def onSceneStatusUpdated(self, sceneStatusInfo: SceneStatusInfo) -> None: pass
