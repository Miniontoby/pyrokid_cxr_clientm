"""com.rokid.cxr.client-m:1.0.9 - extend/infos/RKWifiInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class RKWifiInfo:
	"""com.rokid.cxr.client.extend.infos.RKWifiInfo Java class to Python"""
	name: str
	signal: int
