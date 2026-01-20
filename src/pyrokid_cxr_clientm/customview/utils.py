"""Rokid CXR CustomView Helpers - Util functions"""
import re

def checkForDpValue(value, key: str) -> str:
	if value is None or re.search(r"^\d+dp$", value):
		return value
	if re.search(r"^\d+$", value):
		return value + "dp"
	raise ValueError("%s must be a valid size" % (key))

def checkLayoutValue(value, key: str) -> str:
	if value in ["match_parent", "wrap_content"] or re.search(r"^\d+dp$", value):
		return value
	if re.search(r"^\d+$", value):
		return value + "dp"
	raise ValueError("%s must be 'match_parent', 'wrap_content', or a value ending with 'dp'" % (key))

def checkTrueFalse(value, key: str) -> str|None:
	if value is None: return value
	if isinstance(value, str) and (value.lower() == "true" or value.lower() == "false"): return value.lower()
	if value == True: return "true"
	if value == False: return "false"
	raise ValueError("%s must be None or a valid boolean" % (key))

def excludeOptionalDict(value) -> bool:
	return value is None or not value

def processColorValue(color: str) -> str:
	"""
	When processing color values, if the input is a valid color value, only the green channel is retained.

	:param str color: ARGB or RGB hex string
	"""
	# Check if it is a valid ARGB format (#AARRGGBB)
	if re.search(r"^#[0-9a-fA-F]{8}$", color):
		# Analyzing ARGB channel values
		alpha = color[1:3]
		red = color[3:5]
		green = color[5:7]
		blue = color[7:9]

		# Returns the color value with only the green channel retained, while the red and blue channels are set to 00.
		return "#%s00%s00" % (alpha, green) # '#$alpha${"00"}$green${"00"}'
	# Check if it is a valid RGB format (#RRGGBB)
	elif re.search(r"^#[0-9a-fA-F]{6}$", color):
		# Analyzing RGB channel values
		red = color[1:3]
		green = color[3:5]
		blue = color[5:7]

		# Returns the color value with only the green channel retained, while the red and blue channels are set to 00.
		return "#FF00%s00" % (green)
	# If it is not a valid color format, return the original value.
	else:
		raise ValueError("Invalid color format: %s" % (color))
