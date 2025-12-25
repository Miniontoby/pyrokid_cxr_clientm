from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class SceneStatusInfo:
	"""SceneStatusInfo"""
	aiAssistRunning: bool
	"""Is the aiAssist running?"""
	aiChatRunning: bool
	"""Is the aiChat running?"""
	arPictureRunning: bool
	"""Is the arPicture running?"""
	audioRecordRunning: bool
	"""Is the audioRecord running?"""
	cityGuideRunning: bool
	"""Is the cityGuide running?"""
	customViewRunning: bool
	"""Is the customView running?"""
	hasDisplay: bool
	"""Do we have a display?"""
	liveBroadcastRunning: bool
	"""Are we live broadcasting?"""
	mixRecordRunning: bool
	"""Is the mixRecord running?"""
	musicWordRunning: bool
	"""Is the musicWord running? I guess lyrics display"""
	navigationRunning: bool
	"""Is the navigation running?"""
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
