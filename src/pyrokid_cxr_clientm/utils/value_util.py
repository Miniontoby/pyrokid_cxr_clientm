from enum import IntEnum
try:
	from enum import StrEnum # python 3.11+
except:
	# python <3.11
	from enum import Enum # python <3.11
	class StrEnum(str, Enum): pass	

class ValueUtil:
	"""com.rokid.cxr.client.utils.ValueUtil java class to python"""

	class CxrBluetoothErrorCode(IntEnum):
		SUCCEED = 0
		PARAM_INVALID = 1
		BLE_CONNECT_FAILED = -2
		SOCKET_CONNECT_FAILED = -3
		SN_CHECK_FAILED = -4
		UNKNOWN = -1
		
		def getErrorCode(self) -> int:
			return self.value

	class CxrMediaType(IntEnum):
		AUDIO = 0
		PICTURE = 1
		VIDEO = 2
		ALL = 3
		
		def getType(self) -> int:
			return self.value

	class CxrNotifyType(IntEnum):
		UNKNOWN = 0
		REQUEST = 1
		NOTIFY = 2
		
		def getType(self) -> int:
			return self.value

	class CxrSceneType(StrEnum):
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
		UNKNOWN = -1
		
		def getErrorCode(self) -> int:
			return self.value
	
	class CxrStatus(IntEnum):
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
		WORD_TIPS = 1
		
		def getType(self) -> int:
			return self.value

	class CxrWifiErrorCode(IntEnum):
		SUCCEED = 0
		WIFI_DISABLED = 1
		WIFI_CONNECT_FAILED = -2
		UNKNOWN = -1
		
		def getErrorCode(self) -> int:
			return self.value
