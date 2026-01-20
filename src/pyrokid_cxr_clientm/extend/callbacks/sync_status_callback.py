"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/SyncStatusCallback.java in Python"""

from abc import ABC, abstractmethod

class SyncStatusCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.SyncStatusCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onSyncStart(self) -> None: pass
	@abstractmethod
	def onSingleFileSynced(self, fileName: str) -> None: pass
	@abstractmethod
	def onSyncFailed(self) -> None: pass
	@abstractmethod
	def onSyncFinished(self) -> None: pass
