"""Rokid CustomView Helpers - Props class"""
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional
import re

from .utils import checkForDpValue, checkLayoutValue, checkTrueFalse, excludeOptionalDict

@dataclass_json
@dataclass(frozen=True)
class Props:
	"""Props class"""
	id: str
	layout_width: str = 'match_parent'
	"""Support values: match_parent, wrap_content or a dp number"""
	layout_height: str = 'wrap_content'
	"""Support values: match_parent, wrap_content or a dp number"""

	layout_toStartOf: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""
	layout_above: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""
	layout_toEndOf: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""
	layout_below: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""
	layout_alignBaseLine: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""
	layout_alignStart: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""
	layout_alignEnd: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""
	layout_alignTop: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""
	layout_alignBottom: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Value is supposed to be the id of another child. Only usable when SelfView is a child of a RelativeLayout"""

	layout_alignParentStart: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: true, false. Only usable when SelfView is a child of a RelativeLayout"""
	layout_alignParentEnd: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: true, false. Only usable when SelfView is a child of a RelativeLayout"""
	layout_alignParentTop: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: true, false. Only usable when SelfView is a child of a RelativeLayout"""
	layout_alignParentBottom: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: true, false. Only usable when SelfView is a child of a RelativeLayout"""
	layout_centerInParent: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: true, false. Only usable when SelfView is a child of a RelativeLayout"""
	layout_centerHorizontal: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: true, false. Only usable when SelfView is a child of a RelativeLayout"""
	layout_centerVertical: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	"""Supported values: true, false. Only usable when SelfView is a child of a RelativeLayout"""

	def __post_init__(self):
		if self.id is not None and not re.search(r"^[a-zA-Z0-9_]+$", self.id):
			raise ValueError('id cannot be empty')

		object.__setattr__(self, 'layout_width',  checkLayoutValue(self.layout_width,  'layout_width'))
		object.__setattr__(self, 'layout_height', checkLayoutValue(self.layout_height, 'layout_height'))

		if self.layout_toStartOf is not None and len(self.layout_toStartOf) <= 0:
			raise ValueError('layout_toStartOf cannot be empty')
		if self.layout_above is not None and len(self.layout_above) <= 0:
			raise ValueError('layout_above cannot be empty')
		if self.layout_toEndOf is not None and len(self.layout_toEndOf) <= 0:
			raise ValueError('layout_toEndOf cannot be empty')
		if self.layout_below is not None and len(self.layout_below) <= 0:
			raise ValueError('layout_below cannot be empty')
		if self.layout_alignBaseLine is not None and len(self.layout_alignBaseLine) <= 0:
			raise ValueError('layout_alignBaseLine cannot be empty')
		if self.layout_alignStart is not None and len(self.layout_alignStart) <= 0:
			raise ValueError('layout_alignStart cannot be empty')
		if self.layout_alignEnd is not None and len(self.layout_alignEnd) <= 0:
			raise ValueError('layout_alignEnd cannot be empty')
		if self.layout_alignTop is not None and len(self.layout_alignTop) <= 0:
			raise ValueError('layout_alignTop cannot be empty')
		if self.layout_alignBottom is not None and len(self.layout_alignBottom) <= 0:
			raise ValueError('layout_alignBottom cannot be empty')

		object.__setattr__(self, 'layout_alignParentStart',  checkTrueFalse(self.layout_alignParentStart,  'layout_alignParentStart'))
		object.__setattr__(self, 'layout_alignParentEnd',    checkTrueFalse(self.layout_alignParentEnd,    'layout_alignParentEnd'))
		object.__setattr__(self, 'layout_alignParentTop',    checkTrueFalse(self.layout_alignParentTop,    'layout_alignParentTop'))
		object.__setattr__(self, 'layout_alignParentBottom', checkTrueFalse(self.layout_alignParentBottom, 'layout_alignParentBottom'))
		object.__setattr__(self, 'layout_centerInParent',    checkTrueFalse(self.layout_centerInParent,    'layout_centerInParent'))
		object.__setattr__(self, 'layout_centerHorizontal',  checkTrueFalse(self.layout_centerHorizontal,  'layout_centerHorizontal'))
		object.__setattr__(self, 'layout_centerVertical',    checkTrueFalse(self.layout_centerVertical,    'layout_centerVertical'))

@dataclass_json
@dataclass(frozen=True)
class PropsWithPaddingAndMargin(Props):
	"""PropsWithPaddingAndMargin class"""
	padding: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	paddingStart: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	paddingEnd: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	paddingTop: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	paddingBottom: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	margin: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	marginStart: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	marginEnd: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	marginTop: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)
	marginBottom: Optional[str] = field(metadata=config(exclude=excludeOptionalDict), default=None)

	def __post_init__(self):
		super().__post_init__()

		object.__setattr__(self, 'padding',       checkForDpValue(self.padding,       'padding'))
		object.__setattr__(self, 'paddingStart',  checkForDpValue(self.paddingStart,  'paddingStart'))
		object.__setattr__(self, 'paddingEnd',    checkForDpValue(self.paddingEnd,    'paddingEnd'))
		object.__setattr__(self, 'paddingTop',    checkForDpValue(self.paddingTop,    'paddingTop'))
		object.__setattr__(self, 'paddingBottom', checkForDpValue(self.paddingBottom, 'paddingBottom'))

		object.__setattr__(self, 'margin',        checkForDpValue(self.margin,        'margin'))
		object.__setattr__(self, 'marginStart',   checkForDpValue(self.marginStart,   'marginStart'))
		object.__setattr__(self, 'marginEnd',     checkForDpValue(self.marginEnd,     'marginEnd'))
		object.__setattr__(self, 'marginTop',     checkForDpValue(self.marginTop,     'marginTop'))
		object.__setattr__(self, 'marginBottom',  checkForDpValue(self.marginBottom,  'marginBottom'))


__all__ = ['Props', 'PropsWithPaddingAndMargin']
