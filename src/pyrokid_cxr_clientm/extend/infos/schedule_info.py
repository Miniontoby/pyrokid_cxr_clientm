from dataclasses import dataclass

@dataclass
class ScheduleInfo:
	"""ScheduleInfo"""
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
