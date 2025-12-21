from dataclasses import dataclass

@dataclass
class RKAppInfo:
	"""RKAppInfo"""
	packageName: str
	"""The name of the package of the app"""
	activityName: str
	"""The name of the activity of the app"""
