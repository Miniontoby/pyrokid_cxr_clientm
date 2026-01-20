"""com.rokid.cxr.client-m:1.0.4 - extend/ in Python

extend namespaces contains Constants and a lot of sub-namespaces
"""
__all__ = ['Constants', 'callbacks', 'controllers', 'infos', 'listeners', 'sync', 'version']

from .constants import Constants
from . import callbacks, controllers, infos, listeners, sync, version
