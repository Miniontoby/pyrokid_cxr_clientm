"""Rokid CXR CustomView Helpers - RelativeLayoutProps class"""
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional

from .utils import excludeOptionalDict, processColorValue
from .props import PropsWithPaddingAndMargin

@dataclass_json
@dataclass(frozen=True)
class RelativeLayoutProps(PropsWithPaddingAndMargin):
	"""RelativeLayoutProps class"""
	id: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	backgroundColor: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)

	def __post_init__(self):
		super().__post_init__()

		if not self.backgroundColor is None:
			object.__setattr__(self, 'backgroundColor', processColorValue(self.backgroundColor))

__all__ = ['RelativeLayoutProps']
