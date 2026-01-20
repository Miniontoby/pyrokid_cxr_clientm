"""extend/infos/GlassSettingItem added by me"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class GlassSettingItem:
	"""GlassSettingItem is added by me"""
	key: str
	value: str

# GlassSettingItem.schema().loads('[{"key":"settings_photo_width","value":"4032"},{"key":"settings_photo_height","value":"3024"},{"key":"settings_video_duration","value":"10"},{"key":"settings_video_fps","value":"30"},{"key":"settings_video_width","value":"2400"},{"key":"settings_video_height","value":"1800"},{"key":"settings_sound_effect","value":"AdiMode1"},{"key":"settings_voice_control","value":"close"},{"key":"settings_screen_turnOff","value":"false"},{"key":"settings_screen_offTimeout","value":"5"},{"key":"settings_auto_power_off_turnOn_value","value":"30"},{"key":"settings_auto_power_off_timeout","value":"30"},{"key":"settings_interaction_shortPressFun","value":"picture"},{"key":"settings_interaction_longPressFun","value":"video"},{"key":"settings_language","value":"en-US"},{"key":"settings_country_code","value":"CN"},{"key":"settings_developer_mode","value":"off"},{"key":"settings_launcher_app_list","value":"[brightness, volume, translate, word_tips, music_word, navigation, settings]"},{"key":"settings_camera_power_freq","value":"50"},{"key":"settings_local_tts_param","value":"{\\"voice_id\\":2}"},{"key":"settings_audio_codec_type","value":"3"},{"key":"settings_translate_audio_mode","value":"orientation"},{"key":"settings_wearing_sensitivity","value":"off"},{"key":"settings_local_tts_speed","value":"1"},{"key":"settings_video_duration_unit","value":"0"},{"key":"settings_msg_notification_sound_enabled","value":"true"},{"key":"settings_app_is_overseas","value":"true"},{"key":"settings_msg_notification_display_duration","value":"5"},{"key":"settings_schedule_tts_enabled","value":"true"},{"key":"settings_store_demo_mode_enabled","value":"false"},{"key":"settings_capture_preview_enabled","value":"true"},{"key":"settings_capture_preview_display_duration","value":"3"},{"key":"settings_phone_model","value":"other"},{"key":"settings_shortcuts","value":"true"},{"key":"settings_map_view_visible","value":"1"},{"key":"settings_map_view_align","value":"1"},{"key":"settings_lock_car_view_margin","value":"0"},{"key":"settings_call_playtts_control","value":"false"},{"key":"settings_call_head_control","value":"true"}]', many=True)
# voiceWakeUp = [{"key":"settings_voice_control","value":"open"}] or "value":"close"
