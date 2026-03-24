"""com.rokid.cxr.client-m:1.0.9 - extend/infos/SceneStatusInfo.java in Python"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class SceneStatusInfo:
	"""com.rokid.cxr.client.extend.infos.SceneStatusInfo Java class to Python"""
	aiAssistRunning: bool
	aiChatRunning: bool
	audioRecordRunning: bool
	hasDisplay: bool
	navigationRunning: bool
	otaRunning: bool
	paymentRunning: bool
	phoneCallRunning: bool
	translateRunning: bool
	videoRecordRunning: bool
	wordTipsRunning: bool
	customViewRunning: bool
	mixRecordRunning: bool

	# These are NOT in the original class, but they are provided by the glasses
	arPictureRunning: bool = False
	brightnessRunning: bool = False
	# Does no longer exist
	cityGuideRunning: bool = False
	liveBroadcastRunning: bool = False
	musicWordRunning: bool = False
	notesRunning: bool = False
