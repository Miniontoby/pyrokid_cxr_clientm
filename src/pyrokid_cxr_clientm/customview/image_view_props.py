"""Rokid CXR CustomView Helpers - ImageViewProps class"""
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional

from .utils import *
from .props import Props

@dataclass_json
@dataclass(frozen=True)
class ImageViewProps(Props):
	"""ImageViewProps class"""
	name: str = 'NONE'
	"""Name of a uploaded Icon. Upload icons using the :func:CxrApi.sendCustomViewIcons:"""
	scaleType: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: matrix, fix_xy, fix_start, fix_center, fix_end, center, center_crop, center_inside"""

	def __post_init__(self):
		super().__post_init__()

		if len(self.name) <= 0:
			raise ValueError('name cannot be empty')

		if self.scaleType is not None and not self.scaleType in ['matrix', 'fix_xy', 'fix_start', 'fix_center', 'fix_end', 'center', 'center_crop', 'center_inside']:
			raise ValueError('scaleType must be one of the following: matrix, fix_xy, fix_start, fix_center, fix_end, center, center_crop, center_inside')

__all__ = ['ImageViewProps']
