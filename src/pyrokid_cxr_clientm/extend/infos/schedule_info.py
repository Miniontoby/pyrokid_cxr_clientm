"""com.rokid.cxr.client-m:1.0.4 - extend/infos/ScheduleInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class ScheduleInfo:
	"""com.rokid.cxr.client.extend.infos.ScheduleInfo Java class to Python"""
	id: int
	"""The id of the schedule"""
	title: str = ""
	"""The title of the schedule"""
	description: str = ""
	"""The description of the schedule"""
	scheduleTime: int = 0
	"""The time of the schedule"""
	reminderTime: int = 0
	"""The time of the reminder of the schedule"""
