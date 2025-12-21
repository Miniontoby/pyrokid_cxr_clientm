from dataclasses import dataclass

@dataclass
class IconInfo:
	"""IconInfo. Icons should not exceed 128*128px"""
	name: str
	"""name or identifier of the icon"""
	data: str
	"""base64 field of the icon"""
