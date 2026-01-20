"""com.rokid.cxr.client-m:1.0.4 - extend/infos/RKWifiInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RKWifiInfo:
	"""com.rokid.cxr.client.extend.infos.RKWifiInfo Java class to Python"""
	name: str
	"""The name of the wifi network"""
	signal: int
	"""The signal strength of the wifi network"""
	capabilities: str
	"""The capabilities of the wifi network. E.g.: WPA2-PSK"""
