"""com.rokid.cxr.client-m library for Python

A python port of the com.rokid.cxr.client-m Java library.

The idea is to allow you to use the CXR-M SDK on any device with bluetooth.
"""

__all__ = ['controllers', 'customview', 'extend', 'utils', 'Caps', 'CXRSocketProtocol', 'PacketTypeIds']
from ._version import __version__
__author__ = 'Miniontoby'

from .libcaps import Caps
from .cxr_socket_protocol import CXRSocketProtocol, PacketTypeIds
from . import controllers, customview, extend, utils
