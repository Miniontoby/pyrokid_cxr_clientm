from dataclasses import dataclass

@dataclass
class SceneStatusInfo:
	"""SceneStatusInfo"""
	aiAssistRunning: bool
	"""Is the aiAssist running?"""
	aiChatRunning: bool
	"""Is the aiChat running?"""
	audioRecordRunning: bool
	"""Is the audioRecord running?"""
	brightnessRunning: bool
	"""Is the brightness running?"""
	hasDisplay: bool
	"""Do we have a display?"""
	navigationRunning: bool
	"""Is the navigation running?"""
	notesRunning: bool
	"""Is the notes running?"""
	otaRunning: bool
	"""Is the ota running?"""
	paymentRunning: bool
	"""Is the payment running?"""
	phoneCallRunning: bool
	"""Is the phoneCall running?"""
	translateRunning: bool
	"""Is the translate running?"""
	videoRecordRunning: bool
	"""Is the videoRecord running?"""
	wordTipsRunning: bool
	"""Is the wordTips running?"""
	customViewRunning: bool
	"""Is the customView running?"""
