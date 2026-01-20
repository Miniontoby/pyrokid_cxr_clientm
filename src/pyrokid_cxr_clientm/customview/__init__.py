"""
Rokid's CXR CustomView requires you to make JSON

This namespace will help you making sure you got valid CustomView JSON

This is unofficial code, Rokid doesn't supply any of this!
"""

__all__ = ['LinearLayoutProps', 'RelativeLayoutProps', 'TextViewProps', 'ImageViewProps', 'SelfView', 'UpdateView', 'Props', 'PropsWithPaddingAndMargin']

from .props import Props, PropsWithPaddingAndMargin
from .linear_layout_props import LinearLayoutProps
from .relative_layout_props import RelativeLayoutProps
from .text_view_props import TextViewProps
from .image_view_props import ImageViewProps
from .self_view import SelfView
from .update_view import UpdateView
