"""
com.rokid.cxr.client-m:1.0.9 - CXRSocketProtocol.java in Python

CXRSocketProtocol is the layer that directly connects to the glasses.
It is not supposed to be used directly, as :class:`CxrApi` is supposed to be used to talk back and forth.
"""

from abc import ABC, abstractmethod
from enum import IntEnum
from typing import Callable

from .utils import ValueUtil
from .libcaps import Caps

class PacketTypeIds(IntEnum):
	"""Packet Type IDs used in :class:`CXRSocketProtocol` Requests and Responses"""
	REQUEST = 0x1001 # request
	RESPONSE = 0x1002 # response
	NOTIFY = 0x1003 # notify

	AUTH_REQUEST = 0x1004 # authRequest
	AUTH_RESPONSE = 0x1005 # authResponse
	ROKID_ACCOUNT_REQUEST = 0x1006 # changeRokidAccount

	# Binary transfer related. Ai_TakePhoto for example
	TRANSFER_START = 0x2001
	TRANSFER_DATA = 0x2002
	TRANSFER_END = 0x2003

	# ARTC video frames
	ARTC_START = 0x2011
	ARTC_DATA = 0x2012
	ARTC_END = 0x2013

	# AudioStream frames
	AUDIO_START = 0x3001
	AUDIO_DATA = 0x3002
	AUDIO_END = 0x3003

class CXRSocketProtocol:
	"""com.rokid.cxr.client.CXRSocketProtocol Java class in Python"""
	a: str
	"""mTag"""
	b = None # BluetoothSocket
	c = None # InputStream
	d = None # OutputStream
	e: Callable = None
	f: int = 0
	g: bool = False
	h: bool = False
	i: 'CXRSocketProtocol.Callback' = None
	"""mCallback"""
	j: int
	"""size?"""

	class Callback(ABC):
		"""com.rokid.cxr.client.CXRSocketProtocol.Callback Interface - Please extend this class and implement the methods!"""
		@abstractmethod
		def onResponse(self, reqId: int, args: Caps) -> None: pass
		@abstractmethod
		def onNotify(self, cmd: str, args: Caps) -> None: pass
		@abstractmethod
		def onReceived(self, cmd: str, args: Caps, stream: bytes) -> None: pass
		@abstractmethod
		def onStartAudioStream(self, i: int, codec: int, cmd: str, args: Caps) -> None: pass
		@abstractmethod
		def onAudioStream(self, i: int, data: bytes, offset: int, size: int) -> None: pass
		@abstractmethod
		def onAudioStreamFinish(self, codec: int) -> None: pass
		@abstractmethod
		def onARTCFrame(self, data: bytes) -> None: pass
		@abstractmethod
		def onDisconnect(self) -> None: pass

	def version(self) -> int: return 4

__all__ = ['CXRSocketProtocol', 'PacketTypeIds']
