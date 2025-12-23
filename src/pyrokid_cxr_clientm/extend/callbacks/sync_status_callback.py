class SyncStatusCallback:
	"""SyncStatusCallback Interface - Please extend this class and implement the methods"""
	def onSyncStart(self) -> None: pass
	def onSingleFileSynced(self, paramString: str) -> None: pass
	def onSyncFailed(self) -> None: pass
	def onSyncFinished(self) -> None: pass
