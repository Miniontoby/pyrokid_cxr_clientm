"""Rokid CXR CustomView Helpers - SelfView class"""
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional

from .utils import excludeOptionalDict
from .props import Props

@dataclass_json
@dataclass(frozen=True)
class SelfView:
	"""SelfView class"""
	type: str
	props: Props
	children: Optional[list['SelfView']] = field(metadata=config(exclude=excludeOptionalDict), default=None)

	def __post_init__(self):
		if len(self.type) <= 0:
			raise ValueError("type can not be empty")

		#if not isinstance(self.props, Props):
		#	raise ValueError("props must be of type Props")

__all__ = ['SelfView']
