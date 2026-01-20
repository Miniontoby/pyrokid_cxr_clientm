"""
com.rokid.cxr.client-m:1.0.4 - extend/version/Md5Util.java in Python

Md5Util class is used to do MD5 hashing related to :class:`CheckUtil`
"""

import hashlib
from ...utils import LogUtil

class Md5Util:
	@staticmethod
	def getMd5(content) -> str:
		LogUtil.i("Md5Util", "getMd5: %s", content)
		try:
			md5_hash = hashlib.md5()
			md5_hash.update(content.encode())
			return Md5Util.a(md5_hash.digest())
		except Exception as exception:
			LogUtil.e("Md5Util", exception)
			return None
	
	@staticmethod
	def a(bytes_input: bytes) -> str:
		LogUtil.i("Md5Util", "byteArrayToHex: %s", bytes_input)
		try:
			hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
			char_array = []
			for b1 in bytes_input:
				char_array.append(hex_chars[(b1 >> 4) & 0xF])
				char_array.append(hex_chars[b1 & 0xF])
			return ''.join(char_array)
		except Exception as exception:
			LogUtil.e("Md5Util", exception)
			return None

__all__ = ['Md5Util']
