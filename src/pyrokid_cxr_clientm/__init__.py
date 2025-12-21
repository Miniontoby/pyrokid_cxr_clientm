"""com.rokid.cxr.client-m library for Python

A python port of the com.rokid.cxr.client-m Java library.

The idea is to allow you to use the CXR-M SDK on any device with bluetooth.
"""

__all__ = ['libcaps', 'libcxr-sock-proto-jni']
__version__ = '0.0.3a0'
__author__ = 'Miniontoby'

from .libcaps import *
from .libcxr_sock_proto_jni import *
from .extend import *
