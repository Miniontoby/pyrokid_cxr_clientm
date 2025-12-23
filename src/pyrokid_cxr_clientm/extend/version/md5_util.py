import hashlib
from ...utils import LogUtil

class Md5Util:
	@staticmethod
	def getMd5(paramString) -> str:
		LogUtil.i("Md5Util", "getMd5: %s", paramString)
		try:
			md5_hash = hashlib.md5()
			md5_hash.update(paramString.encode())
			return Md5Util.a(md5_hash.digest())
		except Exception as exception:
			LogUtil.e("Md5Util", exception)
			return None
	
	@staticmethod
	def a(paramArrayOfbyte: bytes) -> str:
		LogUtil.i("Md5Util", "byteArrayToHex: %s", paramArrayOfbyte)
		try:
			hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
			arrayOfChar2 = []
			for b1 in paramArrayOfbyte:
				arrayOfChar2.append(hex_chars[(b1 >> 4) & 0xF])
				arrayOfChar2.append(hex_chars[b1 & 0xF])
			return ''.join(arrayOfChar2)
		except Exception as exception:
			LogUtil.e("Md5Util", exception)
			return None
