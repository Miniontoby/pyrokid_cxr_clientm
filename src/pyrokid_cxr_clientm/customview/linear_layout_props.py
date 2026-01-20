"""Rokid CXR CustomView Helpers - LinearLayoutProps class"""
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional

from .utils import *
from .props import PropsWithPaddingAndMargin

@dataclass_json
@dataclass(frozen=True)
class LinearLayoutProps(PropsWithPaddingAndMargin):
	"""LinearLayoutProps class"""
	id: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	gravity: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: center, center_vertical, center_horizontal, start, end, top, bottom"""
	orientation: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: vertical, horizontal"""
	layout_weight: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	backgroundColor: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)

	def __post_init__(self):
		super().__post_init__()

		if self.gravity is not None and not self.gravity in ['center', 'center_vertical', 'center_horizontal', 'start', 'end', 'top', 'bottom']:
			raise ValueError('gravity must be one of the following: center, center_vertical, center_horizontal, start, end, top, bottom')

		if self.orientation is not None and not self.orientation in ['vertical', 'horizontal']:
			raise ValueError('orientation must be one of the following: vertical, horizontal')

		if not self.backgroundColor is None:
			object.__setattr__(self, 'backgroundColor', processColorValue(self.backgroundColor))

__all__ = ['LinearLayoutProps']
