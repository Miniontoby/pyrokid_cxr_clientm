"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/SceneStatusUpdateListener.java in Python"""

from abc import ABC, abstractmethod
from ..infos import SceneStatusInfo

class SceneStatusUpdateListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.SceneStatusUpdateListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onSceneStatusUpdated(self, sceneStatusInfo: SceneStatusInfo) -> None: pass
