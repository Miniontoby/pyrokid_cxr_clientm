"""com.rokid.cxr.client-m:1.0.9 - utils/LogUtil.java in Python

LogUtil class is used to do logging in the Java library.
In Android code it was already a wrapper for the Android Logger class, and was mostly made because of the setLogLevel method
"""

import logging, traceback

class LogUtil:
	"""com.rokid.cxr.client.utils.LogUtil Java class to Python"""
	VERBOSE: int = 1
	DEBUG: int = 2
	INFO: int = 3
	WARN: int = 4
	ERROR: int = 5
	_modules = {}
	_a: int = 1

	@staticmethod
	def setLogLevel(logLevel: int) -> None:
		"""Sets the log level. But not really used, as logging module already handles logging level..."""
		LogUtil._a = logLevel

	@staticmethod
	def _getLogger(module):
		if not module in LogUtil._modules:
			LogUtil._modules[module] = logging.getLogger(module)
		logger = LogUtil._modules[module]
		#if LogUtil._a <= 1: logger.setLevel(logging.DEBUG) # LogUtil.VERBOSE
		#elif LogUtil._a <= 2: logger.setLevel(logging.DEBUG) # LogUtil.DEBUG
		#elif LogUtil._a <= 3: logger.setLevel(logging.INFO) # LogUtil.INFO
		#elif LogUtil._a <= 4: logger.setLevel(logging.WARNING) # LogUtil.WARN
		#elif LogUtil._a <= 5: logger.setLevel(logging.ERROR) # LogUtil.ERROR
		#else: raise Exception("Unknown Logging Level")
		return logger

	@staticmethod
	def v(module: str, *args, **kwargs):
		"""verbose level logging"""
		#if LogUtil._a <= 1: LogUtil.VERBOSE:
		return LogUtil._getLogger(module).debug(*args, **kwargs)

	@staticmethod
	def d(module: str, *args, **kwargs):
		"""debug level logging"""
		#if LogUtil._a <= 2: LogUtil.DEBUG:
		return LogUtil._getLogger(module).debug(*args, **kwargs)

	@staticmethod
	def i(module: str, *args, **kwargs):
		"""info level logging"""
		#if LogUtil._a <= 3: LogUtil.INFO:
		return LogUtil._getLogger(module).info(*args, **kwargs)

	@staticmethod
	def w(module: str, *args, **kwargs):
		"""warning level logging"""
		#if LogUtil._a <= 4: LogUtil.WARN:
		return LogUtil._getLogger(module).warning(*args, **kwargs)

	@staticmethod
	def e(module: str, param1, *args, **kwargs):
		"""error level logging. When first parameter is an Exception, we'll just print the tracktrace."""
		#if LogUtil._a <= 5: LogUtil.ERROR:
		if isinstance(param1, Exception):
			return LogUtil._getLogger(module).exception("%s", param1, *args, **kwargs)
		return LogUtil._getLogger(module).error(param1, *args, **kwargs)

	@staticmethod
	def getStackTrace(paramException: Exception) -> str:
		return ''.join(traceback.format_exception(paramException))
