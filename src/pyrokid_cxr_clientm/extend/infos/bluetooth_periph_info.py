"""com.rokid.cxr.client-m:1.0.9 - extend/infos/BluetoothPeriphInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class BluetoothPeriphInfo:
	"""com.rokid.cxr.client.extend.infos.BluetoothPeriphInfo Java class to Python"""
	address: str
	bondState: int
	name: str
	type: int
	connectState: bool
