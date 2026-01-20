"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/ApkStatusCallback.java in Python"""

from abc import ABC, abstractmethod

class ApkStatusCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.ApkStatusCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onUploadApkSucceed(self) -> None: pass
	@abstractmethod
	def onUploadApkFailed(self) -> None: pass
	@abstractmethod
	def onInstallApkSucceed(self) -> None: pass
	@abstractmethod
	def onInstallApkFailed(self) -> None: pass
	@abstractmethod
	def onUninstallApkSucceed(self) -> None: pass
	@abstractmethod
	def onUninstallApkFailed(self) -> None: pass
	@abstractmethod
	def onOpenAppSucceed(self) -> None: pass
	@abstractmethod
	def onOpenAppFailed(self) -> None: pass
