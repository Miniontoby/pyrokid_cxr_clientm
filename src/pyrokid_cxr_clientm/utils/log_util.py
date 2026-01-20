"""
com.rokid.cxr.client-m:1.0.4 - utils/LogUtil.java in Python

LogUtil class is used to do logging in the Java library.
In Android code it was already a wrapper for the Android Logger class, and was mostly made because of the setLogLevel method
"""
import logging, traceback

class LogUtil:
	"""com.rokid.cxr.client.utils.LogUtil Java class to Python. Used for logging"""
	_modules = {}
	_a: int

	@staticmethod
	def setLogLevel(logLevel: int) -> None:
		"""sets the log level. Doesn't really change anything at the moment"""
		LogUtil._a = logLevel

	@staticmethod
	def _getLogger(module):
		if not module in LogUtil._modules:
			LogUtil._modules[module] = logging.getLogger(module)
		return LogUtil._modules[module]

	@staticmethod
	def v(module: str, *args, **kwargs):
		"""verbose level logging"""
		return LogUtil._getLogger(module).debug(*args, **kwargs)

	@staticmethod
	def d(module: str, *args, **kwargs):
		"""debug level logging"""
		return LogUtil._getLogger(module).debug(*args, **kwargs)

	@staticmethod
	def i(module: str, *args, **kwargs):
		"""info level logging"""
		return LogUtil._getLogger(module).info(*args, **kwargs)

	@staticmethod
	def w(module: str, *args, **kwargs):
		"""warning level logging"""
		return LogUtil._getLogger(module).warning(*args, **kwargs)

	@staticmethod
	def e(module: str, param1, *args, **kwargs):
		"""error level logging. When first parameter is an Exception, we'll just print the tracktrace."""
		if isinstance(param1, Exception):
			return LogUtil._getLogger(module).exception("%s", param1, *args, **kwargs)
		return LogUtil._getLogger(module).error(param1, *args, **kwargs)

	@staticmethod
	def getStackTrace(paramException: Exception) -> str:
		return ''.join(traceback.format_exception(paramException))
