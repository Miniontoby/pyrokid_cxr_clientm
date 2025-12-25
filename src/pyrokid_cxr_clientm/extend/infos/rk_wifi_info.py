from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RKWifiInfo:
	"""RKWifiInfo"""
	name: str
	"""The name of the wifi network"""
	signal: int
	"""The signal strength of the wifi network"""
