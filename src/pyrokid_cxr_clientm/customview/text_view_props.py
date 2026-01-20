"""Rokid CXR CustomView Helpers - TextViewProps class"""
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional
import re

from .utils import *
from .props import PropsWithPaddingAndMargin

@dataclass_json
@dataclass(frozen=True)
class TextViewProps(PropsWithPaddingAndMargin):
	"""TextViewProps class"""
	text: str = 'NONE'
	textColor: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	textSize: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	gravity: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: center, center_vertical, center_horizontal, start, end, top, bottom"""
	textStyle: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: bold, italic, bold_italic"""

	def __post_init__(self):
		super().__post_init__()

		if not self.textColor is None:
			object.__setattr__(self, 'textColor', processColorValue(self.textColor))

		if not (self.textSize is None or re.search(r"^\d+sp$", self.textSize)):
			if not re.search(r"^\d+$", self.textSize):
				raise ValueError('textSize must be a valid size')
			object.__setattr__(self, 'textSize', str(self.textSize) + 'sp')

		if self.gravity is not None and not self.gravity in ['center', 'center_vertical', 'center_horizontal', 'start', 'end', 'top', 'bottom']:
			raise ValueError('gravity must be one of the following: center, center_vertical, center_horizontal, start, end, top, bottom')

		if self.textStyle is not None and not self.textStyle in ['bold', 'italic', 'bold_italic']:
			raise ValueError('textStyle must be one of the following: bold, italic, bold_italic')

__all__ = ['TextViewProps']
