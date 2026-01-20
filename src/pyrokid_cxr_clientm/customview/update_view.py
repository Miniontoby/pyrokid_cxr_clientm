"""Rokid CXR CustomView Helpers - UpdateView class"""
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Dict

@dataclass_json
@dataclass(frozen=True)
class UpdateView:
	"""UpdateView class"""
	id: str
	action: str = 'update'
	props: Dict[str, str] = field(default_factory=dict)

	def __post_init__(self):
		if len(self.id) <= 0:
			raise ValueError('id can not be empty')

		if self.action is None or not self.action in ['update']:
			raise ValueError('action must be one of the following: update')

		if self.props is None:
			raise ValueError('props can not be empty')

__all__ = ['UpdateView']
