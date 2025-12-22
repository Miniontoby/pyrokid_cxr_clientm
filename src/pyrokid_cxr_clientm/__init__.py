"""com.rokid.cxr.client-m library for Python

A python port of the com.rokid.cxr.client-m Java library.

The idea is to allow you to use the CXR-M SDK on any device with bluetooth.
"""

__all__ = ['controllers', 'extend', 'utils', 'Caps', 'CXRSocketProtocol', 'PacketTypeIds']
__version__ = '0.0.4a0'
__author__ = 'Miniontoby'

#from .controllers import *
from .extend import *
from .utils import *
from .libcaps import Caps
#from .cxr_socket_protocol import CXRSocketProtocol, PacketTypeIds
