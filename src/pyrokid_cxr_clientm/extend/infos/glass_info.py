"""com.rokid.cxr.client-m:1.0.9 - extend/infos/GlassInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GlassInfo:
	"""com.rokid.cxr.client.extend.infos.GlassInfo Java class to Python"""
	deviceName: str
	batteryLevel: int
	isCharging: bool
	devicePanel: str
	brightness: int
	sound: int
	wearingStatus: str
	deviceKey: str
	deviceSecret: str
	deviceTypeId: str
	deviceId: str
	deviceSeed: str
	otaCheckUrl: str
	otaCheckApi: str
	assistVersionName: str
	assistVersionCode: int
	systemVersion: str
	
	# These are NOT in the original class, but they are provided by the glasses
	buildTypeIsUser: bool = False
	displayWidth: int = 480
	displayHeight: int = 640
