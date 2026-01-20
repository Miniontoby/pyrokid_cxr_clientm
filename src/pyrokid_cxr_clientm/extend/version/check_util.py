"""
com.rokid.cxr.client-m:1.0.4 - extend/version/CheckUtil.java in Python

CheckUtil class is used to do glasses firmware version checking
"""

from __future__ import annotations
from time import time, sleep
from json import dumps as json_dumps
from requests import post
from ..infos import GlassInfo
from ...utils import LogUtil
from .md5_util import Md5Util

class CheckUtil:
	"""com.rokid.cxr.client.extend.version.CheckUtil Java class to Python"""
	c = None # HttpURLConnection
	"""POST Request response object"""
	d: GlassInfo = None
	"""Glass Info object"""
	
	@staticmethod
	def getInstance() -> CheckUtil:
		return _a.a
	
	def checkGlassVersion(self, glassInfo: GlassInfo) -> str:
		response = None
		LogUtil.i("CheckUtil", "checkGlassVersion: %s", glassInfo)
		try:
			self.d = glassInfo
			url = self.d.otaCheckUrl + self.d.otaCheckApi
			LogUtil.i("CheckUtil", "checkUrl: %s", url)
			timestamp = int(time()) # is already in seconds
			sign = self.getSignature(timestamp)
			LogUtil.i("CheckUtil", "signature: %s", sign)
			authorization = self.getAuthorization(sign, timestamp)
			LogUtil.i("CheckUtil", "authorization: %s", authorization)
			body = json_dumps({
				"version": self.d.systemVersion,
				"osType": "",
				"cpuType": ""
			})
			LogUtil.i("CheckUtil", "body: %s", body)
			for i in range(0, 5):
				response = self.getResponse(authorization, url, body)
				if response is not None:
					break
				# Retry after 1 second
				try:
					sleep(1)
				except Exception as exception:
					LogUtil.e("CheckUtil", exception)
				LogUtil.i("CheckUtil", "check glass version failed, try count: %d", i)
		except Exception as exception:
			LogUtil.e("CheckUtil", exception)
		return response
	
	def getResponse(self, authorization: str, url: str, body: str) -> str:
		LogUtil.i("CheckUtil", "getResponse")
		try:
			self.c = post(
				url,
				data=body,
				headers={
					"Content-Type": "application/json;charset=utf-8",
					"Authorization": authorization,
				}
			)
			if self.c.status_code == 200:
				response = self.c.text
				LogUtil.i("CheckUtil", "response: %s", response)
				return response
			LogUtil.i("CheckUtil", "network error responseCode: %d", self.c.status_code)
			return self.c.text
		except Exception as exception:
			LogUtil.e("CheckUtil", exception)
			return None
	
	def getAuthorization(self, sign: str, timestamp: int) -> str:
		return "version=1.0;time=%d;sign=%s;key=%s;device_type_id=%s;device_id=%s;service=ota" % (timestamp, sign, self.d.deviceKey, self.d.deviceTypeId, self.d.deviceId)
	
	def getSignature(self, timestamp: int) -> str:
		return Md5Util.getMd5("key=%s&device_type_id=%s&device_id=%s&service=ota&version=1.0&time=%d&secret=%s" % (self.d.deviceKey, self.d.deviceTypeId, self.d.deviceId, timestamp, self.d.deviceSecret))

class _a: a: CheckUtil = CheckUtil()
