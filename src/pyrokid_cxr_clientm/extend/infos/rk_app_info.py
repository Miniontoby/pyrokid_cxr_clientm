"""com.rokid.cxr.client-m:1.0.9 - extend/infos/RKAppInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class RKAppInfo:
	"""com.rokid.cxr.client.extend.infos.RKAppInfo Java class to Python"""
	packageName: str
	activityName: str
