"""
com.rokid.cxr.client-m:1.0.4 - extend/sync/HeaderInterceptor.java in Python

HeaderInterceptor is just a function returning headers, nothing special
"""

def HeaderInterceptor(appVersion: str, apiVersion: str) -> dict[str, str]:
	"""
	com.rokid.cxr.client.extend.sync.BaseNetworkResponse Java class to Python function
	:param str appVersion: App version. E.g.: 1.0
	:param str apiVersion: API version. E.g.: 1.0
	"""
	return {
		"appVersion": appVersion,
		"apiVersion": apiVersion
	}
