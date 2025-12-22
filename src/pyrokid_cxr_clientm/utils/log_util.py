import logging, traceback

class LogUtil:
    """Logging Util"""
    _modules = {}
    _a: int

    @staticmethod
    def setLogLevel(paramInt: int) -> None:
        LogUtil._a = paramInt

    @staticmethod
    def _getLogger(module):
        if not module in LogUtil._modules:
            LogUtil._modules[module] = logging.getLogger(module)
        return LogUtil._modules[module]

    @staticmethod
    def v(module: str, *args, **kwargs):
        """verbose logging"""
        return LogUtil._getLogger(module).debug(*args, **kwargs)

    @staticmethod
    def d(module: str, *args, **kwargs):
        """debug logging"""
        return LogUtil._getLogger(module).debug(*args, **kwargs)

    @staticmethod
    def i(module: str, *args, **kwargs):
        """info logging"""
        return LogUtil._getLogger(module).info(*args, **kwargs)

    @staticmethod
    def w(module: str, *args, **kwargs):
        """warning logging"""
        return LogUtil._getLogger(module).warning(*args, **kwargs)

    @staticmethod
    def e(module: str, param1, *args, **kwargs):
        """error logging"""
        if isinstance(param1, Exception):
            return LogUtil._getLogger(module).exception("%s", param1, *args, **kwargs)
        return LogUtil._getLogger(module).error(param1, *args, **kwargs)

    @staticmethod
    def getStackTrace(paramException: Exception) -> str:
        return ''.join(traceback.format_exception(paramException))
