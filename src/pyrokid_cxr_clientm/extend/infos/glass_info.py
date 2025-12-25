from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class GlassInfo:
	"""GlassInfo"""
	deviceName: str
	"""The name of the device"""
	batteryLevel: int
	"""The batteryLevel of the device"""
	isCharging: bool
	"""Is the battery being charged"""
	devicePanel: str
	"""???"""
	brightness: int
	"""The brightness of the device"""
	sound: int
	"""The volume of the device"""
	wearingStatus: str
	"""The wearing status of the device"""
	deviceKey: str
	"""The key of the device"""
	deviceSecret: str
	"""The secret of the device"""
	deviceTypeId: str
	"""The type id of the device"""
	deviceId: str
	"""The id of the device"""
	deviceSeed: str
	"""The seed of the device"""
	otaCheckUrl: str
	"""The OTA check URL of the device"""
	otaCheckApi: str
	"""The OTA check API of the device"""
	assistVersionName: str
	"""The version name of the assistant"""
	assistVersionCode: int
	"""The version code of the assistant"""
	systemVersion: str
	"""The version of the system"""
	displayWidth: int = 481
	"""The width of the display"""
	displayHeight: int = 640
	"""The height of the display"""
