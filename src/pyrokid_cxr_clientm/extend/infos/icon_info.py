from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class IconInfo:
	"""
	Icons should not exceed 128x128px.
	It is recommended to not upload more than 10 icons to keep speed.
	
	Transparent AND black pixels are ignored by the glasses!
	Please use green or white pixels to get visible content!
	Don't even try to open an issue if you're using a black image!

	.. code-block:: python

		from base64 import b64encode
		from pyrokid_cxr_clientm.extend.infos import IconInfo
		
		with open('icon0.png', 'rb') as f:
			icon0_base64 = b64encode(f.read()).decode('utf-8')
		
		icon0 = IconInfo(name='icon0', data=icon0_base64)
	"""
	name: str
	"""The name/identifier of the icon"""
	data: str
	"""The base64 string representation of the icon"""
