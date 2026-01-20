"""com.rokid.cxr.client-m:1.0.4 - extend/callbacks/SendStatusCallback.java in Python"""

from abc import ABC, abstractmethod
from ...utils import ValueUtil

class SendStatusCallback(ABC):
	"""com.rokid.cxr.client.extend.callbacks.SendStatusCallback Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onSendSucceed(self) -> None: pass
	@abstractmethod
	def onSendFailed(self, errorCode: ValueUtil.CxrSendErrorCode) -> None: pass
