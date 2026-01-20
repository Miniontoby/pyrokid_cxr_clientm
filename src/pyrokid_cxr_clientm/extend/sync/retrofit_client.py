"""
com.rokid.cxr.client-m:1.0.4 - extend/sync/RetrofitClient.java in Python

RetrofitClient class is the way how the SDK talks to the HTTP Api
"""

from __future__ import annotations
from ...utils import LogUtil
from .header_interceptor import HeaderInterceptor
from .retrofit_service import RetrofitService

class RetrofitClient:
	"""com.rokid.cxr.client.extend.sync.RetrofitClient Java class to Python"""
	a: RetrofitService = None

	def __init__(self):
		LogUtil.i("RetrofitClient", "RetrofitClient constructed")

	@staticmethod
	def getInstance() -> RetrofitClient:
		LogUtil.v("RetrofitClient", "getInstance")
		return _a.a

	@staticmethod
	def createPartFromString(string: str):
		LogUtil.i("RetrofitClient", "createPartFromString")
		return string

	@staticmethod
	def createPartFromApk(file: str):
		LogUtil.i("RetrofitClient", "createPartFromApk")
		return file

	def setBaseUrl(self, baseUrl: str):
		LogUtil.i("RetrofitClient", "setBaseUrl baseUrl: %s", baseUrl)
		LogUtil.i("RetrofitClient", "createOkHttpClient")
		self.a = RetrofitService(baseUrl, HeaderInterceptor("1.0", "1.0"))

	def getService(self) -> RetrofitService:
		LogUtil.v("RetrofitClient", "getService")
		return self.a

class _a: a: RetrofitClient = RetrofitClient()

__all__ = ['RetrofitClient']
