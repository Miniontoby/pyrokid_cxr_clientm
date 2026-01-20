"""com.rokid.cxr.client-m:1.0.4 - extend/infos/RKAppInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RKAppInfo:
	"""com.rokid.cxr.client.extend.infos.RKAppInfo Java class to Python"""
	packageName: str
	"""The name of the package of the app"""
	activityName: str
	"""The name of the activity of the app"""
