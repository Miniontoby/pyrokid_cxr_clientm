"""
com.rokid.cxr.client-m:1.0.9 - extend/ in Python

extend namespace contains :class:`BuildConfig` and :class:`Constants`
"""

__all__ = ['BuildConfig', 'Constants', 'callbacks', 'controllers', 'infos', 'listeners', 'sync', 'version']

from .build_config import BuildConfig
from .constants import Constants
from . import callbacks, controllers, infos, listeners, sync, version
