"""com.rokid.cxr.client-m:1.0.9 - extend/infos/ScheduleInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ScheduleInfo:
	"""com.rokid.cxr.client.extend.infos.ScheduleInfo Java class to Python"""
	id: int
	title: str = ""
	description: str = ""
	scheduleTime: int = 0
	reminderTime: int = 0
