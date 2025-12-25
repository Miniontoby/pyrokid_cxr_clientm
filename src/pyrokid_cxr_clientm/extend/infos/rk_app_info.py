from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RKAppInfo:
	"""RKAppInfo"""
	packageName: str
	"""The name of the package of the app"""
	activityName: str
	"""The name of the activity of the app"""
