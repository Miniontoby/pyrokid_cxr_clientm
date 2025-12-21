from dataclasses import dataclass

@dataclass
class RKWifiInfo:
	"""RKWifiInfo"""
	name: str
	"""The name of the wifi network"""
	signal: int
	"""The signal strength of the wifi network"""
