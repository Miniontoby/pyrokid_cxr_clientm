"""
libcxr-sock-proto-jni.so to python, kinda
"""
from enum import IntEnum

class PacketTypeIds(IntEnum):
	"""Packet Type IDs used in :type:`CXRSocketProtocol` Requests and Responses"""
	REQUEST = 0x1001 # request
	RESPONSE = 0x1002 # response

	AUTH_REQUEST = 0x1004 # authRequest
	AUTH_RESPONSE = 0x1005 # authResponse
	CHANGE_ROKID_ACCOUNT = 0x1006 # changeRokidAccount

	# These I don't know yet.
	TRANSFER_INFO = 0x2001
	TRANSFER_INFO_TWO = 0x2002
	TRANSFER_INFO_THREE = 0x2003


