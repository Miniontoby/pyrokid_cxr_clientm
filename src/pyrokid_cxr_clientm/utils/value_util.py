"""
com.rokid.cxr.client-m:1.0.4 - utils/ValueUtil.java in Python

ValueUtil class contains all the Cxr Enums
"""

from enum import IntEnum
try:
	from enum import StrEnum # python 3.11+
except:
	# python <3.11
	from enum import Enum # python <3.11
	class StrEnum(str, Enum): pass	

class ValueUtil:
	"""com.rokid.cxr.client.utils.ValueUtil Java class to Python"""

	class CxrBluetoothErrorCode(IntEnum):
		"""com.rokid.cxr.client.utils.ValueUtil.CxrBluetoothErrorCode Java enum to Python"""
		SUCCEED = 0
		PARAM_INVALID = 1
		BLE_CONNECT_FAILED = -2
		SOCKET_CONNECT_FAILED = -3
		SN_CHECK_FAILED = -4
		UNKNOWN = -1
		
		def getErrorCode(self) -> int:
			return self.value

	class CxrMediaType(IntEnum):
		"""com.rokid.cxr.client.utils.ValueUtil.CxrMediaType Java enum to Python"""
		AUDIO = 0
		"""Audio files"""
		PICTURE = 1
		"""Picture files"""
		VIDEO = 2
		"""Video files"""
		ALL = 3
		"""All files"""
		
		def getType(self) -> int:
			return self.value

	class CxrNotifyType(IntEnum):
		"""com.rokid.cxr.client.utils.ValueUtil.CxrNotifyType Java enum to Python"""
		UNKNOWN = 0
		REQUEST = 1
		NOTIFY = 2
		
		def getType(self) -> int:
			return self.value

	class CxrSceneType(StrEnum):
		"""com.rokid.cxr.client.utils.ValueUtil.CxrSceneType Java enum to Python"""
		AI_CHAT = "ai_chat"
		"""Doesn't do anything yet, just says: `This feature is currently unavailable. Stay tuned`"""
		TRANSLATE = "translate"
		"""Opens the translator"""
		AUDIO_RECORD = "audio_record"
		"""Starts an audio recording"""
		VIDEO_RECORD = "video_record"
		"""Starts a video recording"""
		WORD_TIPS = "word_tips"
		"""Opens the teleprompter"""
		NAVIGATION = "navigation"
		"""Opens the navigation app"""
		
		def getSceneId(self) -> str:
			return self.value
	
	class CxrSendErrorCode(IntEnum):
		"""com.rokid.cxr.client.utils.ValueUtil.CxrSendErrorCode Java enum to Python"""
		UNKNOWN = -1
		
		def getErrorCode(self) -> int:
			return self.value
	
	class CxrStatus(IntEnum):
		"""com.rokid.cxr.client.utils.ValueUtil.CxrStatus Java enum to Python"""
		BLUETOOTH_AVAILABLE = 0
		BLUETOOTH_UNAVAILABLE = 1
		BLUETOOTH_INIT = -2
		WIFI_AVAILABLE = 2
		WIFI_UNAVAILABLE = 3
		WIFI_INIT = -2
		REQUEST_SUCCEED = 4
		REQUEST_FAILED = 5
		REQUEST_WAITING = -2
		RESPONSE_SUCCEED = 6
		RESPONSE_INVALID = 7
		RESPONSE_TIMEOUT = -2
		
		def getStatus(self) -> int:
			return self.value

	class CxrStreamType(IntEnum):
		"""com.rokid.cxr.client.utils.ValueUtil.CxrStreamType Java enum to Python"""
		WORD_TIPS = 1
		"""Teleprompter text"""
		
		def getType(self) -> int:
			return self.value

	class CxrWifiErrorCode(IntEnum):
		"""com.rokid.cxr.client.utils.ValueUtil.CxrWifiErrorCode Java enum to Python"""
		SUCCEED = 0
		WIFI_DISABLED = 1
		WIFI_CONNECT_FAILED = -2
		UNKNOWN = -1
		
		def getErrorCode(self) -> int:
			return self.value
