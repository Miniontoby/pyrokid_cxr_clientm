from __future__ import annotations
from time import time, sleep
from json import dumps as json_dumps
from requests import post
from ..infos import GlassInfo
from ...utils import LogUtil
from .md5_util import Md5Util

class CheckUtil:
	a = None # PrintWriter
	b = None # BufferedReader
	c = None # HttpURLConnection
	d: GlassInfo = None
	
	@staticmethod
	def getInstance() -> CheckUtil:
		return _a.a
	
	def checkGlassVersion(self, paramGlassInfo: GlassInfo) -> str:
		strValue = None
		LogUtil.i("CheckUtil", "checkGlassVersion: %s", paramGlassInfo)
		try:
			self.d = paramGlassInfo
			str1 = self.d.otaCheckUrl + self.d.otaCheckApi
			LogUtil.i("CheckUtil", "checkUrl: %s", str1)
			l = int(time())
			str4 = self.getSignature(l)
			LogUtil.i("CheckUtil", "signature: %s", str4)
			str2 = self.getAuthorization(str4, l)
			LogUtil.i("CheckUtil", "authorization: %s", str2)
			str3 = json_dumps({
				"version": self.d.systemVersion,
				"osType": "",
				"cpuType": ""
			})
			LogUtil.i("CheckUtil", "body: %s", str3)
			for i in range(0, 5):
				strValue = self.getResponse(str2, str1, str3)
				if strValue is not None:
					break
				# Retry after 1 second
				try:
					sleep(1)
				except Exception as exception:
					LogUtil.e("CheckUtil", exception)
				LogUtil.i("CheckUtil", "check glass version failed, try count: %d", i)
		except Exception as exception:
			LogUtil.e("CheckUtil", exception)
		return strValue
	
	def getResponse(self, paramString1: str, paramString2: str, paramString3: str) -> str:
		LogUtil.i("CheckUtil", "getResponse")
		try:
			self.c = post(
				paramString2,
				data=paramString3,
				headers={
					"Content-Type": "application/json;charset=utf-8",
					"Authorization": paramString1,
				}
			)
			if self.c.status_code == 200:
				strValue = self.c.text
				LogUtil.i("CheckUtil", "response: %s", strValue)
				return strValue
			LogUtil.i("CheckUtil", "network error responseCode: %d", self.c.status_code)
			return self.c.text
		except Exception as exception:
			LogUtil.e("CheckUtil", exception)
			return None
	
	def getAuthorization(self, paramString: str, paramLong: int) -> str:
		return "version=1.0;time=%d;sign=%s;key=%s;device_type_id=%s;device_id=%s;service=ota" % (paramLong, paramString, self.d.deviceKey, self.d.deviceTypeId, self.d.deviceId)
	
	def getSignature(self, paramLong: int) -> str:
		return Md5Util.getMd5("key=%s&device_type_id=%s&device_id=%s&service=ota&version=1.0&time=%d&secret=%s" % (self.d.deviceKey, self.d.deviceTypeId, self.d.deviceId, paramLong, self.d.deviceSecret))

class _a:
	a: CheckUtil = CheckUtil()
