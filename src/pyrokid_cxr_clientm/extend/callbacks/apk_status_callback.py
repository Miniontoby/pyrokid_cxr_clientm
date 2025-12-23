class ApkStatusCallback:
	"""ApkStatusCallback Interface - Please extend this class and implement the methods"""
	def onUploadApkSucceed(self) -> None: pass
	def onUploadApkFailed(self) -> None: pass
	def onInstallApkSucceed(self) -> None: pass
	def onInstallApkFailed(self) -> None: pass
	def onUninstallApkSucceed(self) -> None: pass
	def onUninstallApkFailed(self) -> None: pass
	def onOpenAppSucceed(self) -> None: pass
	def onOpenAppFailed(self) -> None: pass
