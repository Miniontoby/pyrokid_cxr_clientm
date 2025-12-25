from __future__ import annotations
from ...utils import LogUtil
from .header_interceptor import HeaderInterceptor
from .retrofit_service import RetrofitService

class RetrofitClient:
	a: RetrofitService = None
	def __init__(self):
		LogUtil.i("RetrofitClient", "RetrofitClient constructed");

	@staticmethod
	def getInstance() -> RetrofitClient:
		LogUtil.v("RetrofitClient", "getInstance")
		return _a.a

	@staticmethod
	def createPartFromString(paramString: str):
		LogUtil.i("RetrofitClient", "createPartFromString")
		return paramString

	@staticmethod
	def createPartFromApk(paramFile: str):
		LogUtil.i("RetrofitClient", "createPartFromApk")
		return paramFile

	def setBaseUrl(self, baseUrl: str):
		LogUtil.i("RetrofitClient", "setBaseUrl baseUrl: %s", baseUrl)
		LogUtil.i("RetrofitClient", "createOkHttpClient")
		self.a = RetrofitService(baseUrl, HeaderInterceptor("1.0", "1.0"))

	def getService(self) -> RetrofitService:
		LogUtil.v("RetrofitClient", "getService")
		return self.a

class _a: a: RetrofitClient = RetrofitClient()
