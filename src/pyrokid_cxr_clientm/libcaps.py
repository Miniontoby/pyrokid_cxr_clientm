"""
com.rokid.cxr.client-m:1.0.4 - jni/arm64-v8a/libcaps.so library in Python

Caps class is THE way to decode and encode packets when communicating to the Rokid Glasses.
"""
from __future__ import annotations
from struct import pack as struct_pack, unpack as struct_unpack
from io import BytesIO

class Caps:
	"""Main Caps container class for serialization/deserialization

	:param Optional[list[Caps.Value]] values: Optional values list, in case you already have a list of :type:`Caps.Value`'s.
		Else its recommended to use :func:`Caps.fromBytes`
	"""
	
	CAPS_VERSION = 5
	"""Current Caps version."""

	class CapsError(Exception):
		"""Base exception for :type:`Caps` operations"""
		pass

	class IncorrectTypeException(RuntimeError):
		"""Exception that throws when Type of a :type:`Caps.Value` is not what you were expecting"""
		pass

	__a: list[Caps.Value]
	
	def write(self, value: Any = None) -> Caps:
		"""Add a value to the Caps object"""
		if isinstance(value, Caps.Value):
			self.__a.append(value)
		else:
			self.__a.append(Caps.Value(None, value))
		return self
	
	def writeInt32(self, value: int) -> Caps:
		"""Write an integer value"""
		return self.write(Caps.Value(Caps.Value.TYPE_INT32, int(value)))
	
	def writeUInt32(self, value: int) -> Caps:
		"""Write an unsigned integer value"""
		return self.write(Caps.Value(Caps.Value.TYPE_UINT32, int(value)))
	
	def writeInt64(self, value: int) -> Caps:
		"""Write a long integer value"""
		return self.write(Caps.Value(Caps.Value.TYPE_INT64, int(value)))
	
	def writeUInt64(self, value: int) -> Caps:
		"""Write an unsigned long value"""
		return self.write(Caps.Value(Caps.Value.TYPE_UINT64, int(value)))
	
	def writeFloat(self, value: float) -> Caps:
		"""Write a float value"""
		return self.write(Caps.Value(Caps.Value.TYPE_FLOAT, float(value)))
	
	def writeDouble(self, value: float) -> Caps:
		"""Write a double value"""
		return self.write(Caps.Value(Caps.Value.TYPE_DOUBLE, float(value)))
	
	def writeObject(self, value: Caps) -> Caps:
		"""Write a nested :type:`Caps` object"""
		return self.write(Caps.Value(Caps.Value.TYPE_OBJECT, value))
	
	def writeVoid(self) -> Caps:
		"""Write a void value"""
		return self.write(Caps.Value(Caps.Value.TYPE_VOID, None))
	
	def writeString(self, value: str) -> Caps:
		"""Write a string value"""
		return self.write(Caps.Value(Caps.Value.TYPE_STRING, str(value)))
	
	def writeBoolean(self, value: bool) -> Caps:
		"""Write a void value"""
		return self.write(Caps.Value(Caps.Value.TYPE_UINT32, int(value)))
	
	def writeBinary(self, value: bytes) -> Caps:
		"""Write binary data"""
		return self.write(Caps.Value(Caps.Value.TYPE_BINARY, value))
	
	def __init__(self, values: list[Caps.Value] = None):
		self.__a: list[Caps.Value] = values or []
	
	@staticmethod
	def fromBytes(data: bytes) -> tuple[Caps, bytes]:
		"""Parse a new Caps object from bytes"""
		caps = Caps()
		return caps.parse(data)

	def __repr__(self) -> str:
		return "Caps(%s)" % self.__a
	
	def dump(self) -> str:
		return repr(self)
	
	def serialize(self) -> bytes:
		"""
		Serialize the Caps object to bytes
		Format: [4 bytes size][1 byte version][member descriptors][member data]
		"""
		# First pass: serialize member descriptors and data
		desc_buffer = BytesIO()
		data_buffer = BytesIO()
		
		# Write member count as ULEB128
		desc_buffer.write(Caps._encode_uleb128(len(self.__a)))
		
		# Write type descriptors
		for member in self.__a:
			if not isinstance(member, Caps.Value): continue
			member_type = member.type()
			desc_buffer.write(bytes([member_type]))
		
		# Write member data
		for member in self.__a:
			if not isinstance(member, Caps.Value): continue
			Caps._serialize_member(member, data_buffer)
		
		# Combine everything
		desc_data = desc_buffer.getvalue()
		member_data = data_buffer.getvalue()
		
		total_size = 5 + len(desc_data) + len(member_data)
		
		result = BytesIO()
		result.write(struct_pack('>I', total_size))  # Big-endian size
		result.write(bytes([Caps.CAPS_VERSION]))
		result.write(desc_data)
		result.write(member_data)
		
		return result.getvalue()
	
	def parse(self, data: bytes) -> tuple['Caps', bytes]:
		"""Parse a bytes to the current Caps object"""
		if len(data) < 5:
			raise Caps.CapsError("Data too small")
		
		# Parse header
		size = struct_unpack('>I', data[0:4])[0]
		version = data[4]
		
		if version != Caps.CAPS_VERSION:
			raise Caps.CapsError("Unsupported version: %d" % (version))
		
		if size > len(data):
			raise Caps.CapsError("Size mismatch: expected %d, got %d" % (size, len(data)))
		
		# Parse members
		buffer = BytesIO(data[5:])
		
		# Read member count
		member_count, bytes_read = Caps._decode_uleb128(buffer)
		
		# Read type descriptors
		descriptors = []
		for _ in range(member_count):
			desc = buffer.read(1)
			if not desc:
				raise Caps.CapsError("Truncated descriptor data")
			descriptors.append(desc[0])
		
		# Read member data
		for desc in descriptors:
			value = Caps._parse_member(desc, buffer)
			self.__a.append(Caps.Value(desc, value))

		return self, data[size:] # return the unparsed bytes ;)
	
	def __len__(self) -> int:
		"""Return the number of members"""
		return len(self.__a)
	
	def size(self) -> int:
		"""Return the number of members"""
		return self.__len__()
	
	def __getitem__(self, index: int) -> Caps.Value:
		"""Get member value by index"""
		if index < 0 or index >= len(self.__a):
			raise IndexError("Index out of range")
		return self.__a[index]
	
	def at(self, index: int) -> Caps.Value:
		"""Get member value by index"""
		return self.__getitem__(index)
	
	def clear(self) -> None:
		"""Clear all members"""
		self.__a.clear()
	
	def __str__(self) -> str:
		return self.dump()
	
	def toString(self) -> str:
		return self.dump()
	
	@staticmethod
	def _serialize_member(member: Caps.Value, buffer: BytesIO) -> None:
		"""Serialize a single member's data"""
		member_type = member.type()
		value = member.getValueNoType()
		
		if member_type == Caps.Value.TYPE_VOID:
			pass  # No data
		elif member_type == Caps.Value.TYPE_INT32:
			buffer.write(Caps._encode_sleb128(value))
		elif member_type == Caps.Value.TYPE_UINT32:
			buffer.write(Caps._encode_uleb128(value))
		elif member_type == Caps.Value.TYPE_FLOAT:
			buffer.write(struct_pack('<f', value))
		elif member_type == Caps.Value.TYPE_INT64:
			buffer.write(Caps._encode_sleb128(value))
		elif member_type == Caps.Value.TYPE_UINT64:
			buffer.write(Caps._encode_uleb128(value))
		elif member_type == Caps.Value.TYPE_DOUBLE:
			buffer.write(struct_pack('<d', value))
		elif member_type == Caps.Value.TYPE_STRING:
			encoded = value.encode('utf-8')
			buffer.write(Caps._encode_uleb128(len(encoded)))
			buffer.write(encoded)
		elif member_type == Caps.Value.TYPE_BINARY:
			buffer.write(Caps._encode_uleb128(len(value)))
			buffer.write(value)
		elif member_type == Caps.Value.TYPE_OBJECT:
			nested_data = value.serialize()
			buffer.write(nested_data)
		else:
			raise Caps.CapsError("Unknown member type: %d" % (member_type))
	
	@staticmethod
	def _parse_member(member_type: chr, buffer: BytesIO) -> Any:
		"""Parse a single member from the buffer"""
		if member_type == Caps.Value.TYPE_VOID:
			return None
		elif member_type == Caps.Value.TYPE_INT32:
			value, _ = Caps._decode_sleb128(buffer)
			return value
		elif member_type == Caps.Value.TYPE_UINT32:
			value, _ = Caps._decode_uleb128(buffer)
			return value
		elif member_type == Caps.Value.TYPE_FLOAT:
			data = buffer.read(4)
			return struct_unpack('<f', data)[0]
		elif member_type == Caps.Value.TYPE_INT64:
			value, _ = Caps._decode_sleb128(buffer)
			return value
		elif member_type == Caps.Value.TYPE_UINT64:
			value, _ = Caps._decode_uleb128(buffer)
			return value
		elif member_type == Caps.Value.TYPE_DOUBLE:
			data = buffer.read(8)
			return struct_unpack('<d', data)[0]
		elif member_type == Caps.Value.TYPE_STRING:
			length, _ = Caps._decode_uleb128(buffer)
			data = buffer.read(length)
			return data.decode('utf-8')
		elif member_type == Caps.Value.TYPE_BINARY:
			length, _ = Caps._decode_uleb128(buffer)
			return buffer.read(length)
		elif member_type == Caps.Value.TYPE_OBJECT:
			# Read size header
			size_data = buffer.read(4)
			size = struct_unpack('>I', size_data)[0]
			# Read rest of caps data
			caps_data = size_data + buffer.read(size - 4)
			cls, _ = Caps.fromBytes(caps_data)
			return cls
		else:
			raise Caps.CapsError("Unknown member type: %d" % (member_type))
	
	@staticmethod
	def _encode_uleb128(value: int) -> bytes:
		"""Encode unsigned integer as ULEB128"""
		if value < 0:
			raise ValueError("ULEB128 requires non-negative value")
			
		result = bytearray()
		while True:
			byte = value & 0x7F
			value >>= 7
			if value != 0:
				byte |= 0x80
			result.append(byte)
			if value == 0:
				break
		return bytes(result)
	
	@staticmethod
	def _decode_uleb128(buffer: BytesIO) -> tuple[int, int]:
		"""Decode ULEB128 from buffer, returns (value, bytes_read)"""
		result = 0
		shift = 0
		bytes_read = 0
		
		while True:
			byte_data = buffer.read(1)
			if not byte_data:
				raise Caps.CapsError("Truncated ULEB128")
			byte = byte_data[0]
			bytes_read += 1
			
			result |= (byte & 0x7F) << shift
			shift += 7
			
			if (byte & 0x80) == 0:
				break
				
			if shift >= 64:
				raise Caps.CapsError("ULEB128 too large")
				
		return result, bytes_read
	
	@staticmethod
	def _encode_sleb128(value: int) -> bytes:
		"""Encode signed integer as SLEB128"""
		result = bytearray()
		while True:
			byte = value & 0x7F
			value >>= 7
			# Sign extend
			if value == 0 and (byte & 0x40) == 0:
				result.append(byte)
				break
			elif value == -1 and (byte & 0x40) != 0:
				result.append(byte)
				break
			else:
				result.append(byte | 0x80)
		return bytes(result)
	
	@staticmethod
	def _decode_sleb128(buffer: BytesIO) -> tuple[int, int]:
		"""Decode SLEB128 from buffer, returns (value, bytes_read)"""
		result = 0
		shift = 0
		bytes_read = 0
		byte = 0x80
		
		while (byte & 0x80) != 0:
			byte_data = buffer.read(1)
			if not byte_data:
				raise Caps.CapsError("Truncated SLEB128")
			byte = byte_data[0]
			bytes_read += 1
			
			result |= (byte & 0x7F) << shift
			shift += 7
			
		# Sign extend
		if shift < 64 and (byte & 0x40) != 0:
			result |= -(1 << shift)
			
		return result, bytes_read

	class Value:
		"""Represents a single value in :type:`Caps` format"""
		TYPE_VOID = ord('V')  # 0x56
		TYPE_INT32 = ord('i')  # 0x69
		TYPE_UINT32 = ord('u')  # 0x75
		TYPE_FLOAT = ord('f')  # 0x66
		TYPE_INT64 = ord('l')  # 0x6c
		TYPE_UINT64 = ord('k')  # 0x6b
		TYPE_DOUBLE = ord('d')  # 0x64
		TYPE_STRING = ord('S')  # 0x53
		TYPE_BINARY = ord('B')  # 0x42
		TYPE_OBJECT = ord('O')  # 0x4f
		
		def __init__(self, vType: chr = None, value: Any = None):
			self.__vType = vType
			self.__a = value
		
		def type(self) -> chr:
			"""Determine the type code for this value"""
			if self.__vType:
				return self.__vType
				
			if self.__a is None:
				return Caps.Value.TYPE_VOID
			elif isinstance(self.__a, bool):
				return Caps.Value.TYPE_UINT32
			elif isinstance(self.__a, int):
				if -2**31 <= self.__a < 2**31:
					return Caps.Value.TYPE_INT32
				elif 0 <= self.__a < 2**32:
					return Caps.Value.TYPE_UINT32
				elif -2**63 <= self.__a < 2**63:
					return Caps.Value.TYPE_INT64
				else:
					return Caps.Value.TYPE_UINT64
			elif isinstance(self.__a, float):
				return Caps.Value.TYPE_FLOAT # Or double
			elif isinstance(self.__a, str):
				return Caps.Value.TYPE_STRING
			elif isinstance(self.__a, (bytes, bytearray)):
				return Caps.Value.TYPE_BINARY
			elif isinstance(self.__a, Caps):
				return Caps.Value.TYPE_OBJECT
			else:
				raise CapsError("Unsupported type: %s" % (type(self.__a)))

		def getValueNoType(self) -> Any:
			return self.__a

		def getInt(self) -> int:
			"""Validate if value is int/IN32/UINT32 and return it"""
			if self.type() == Caps.Value.TYPE_INT32 or self.type() == Caps.Value.TYPE_UINT32: return int(self.__a)
			raise Caps.IncorrectTypeException()
		
		def getLong(self) -> int:
			"""Validate if value is long/INT64/UINT64 and return it"""
			if self.type() == Caps.Value.TYPE_INT64 or self.type() == Caps.Value.TYPE_UINT64: return int(self.__a)
			raise Caps.IncorrectTypeException()
		
		def getFloat(self) -> float:
			"""Validate if value is float/FLOAT and return it"""
			if self.type() == Caps.Value.TYPE_FLOAT: return float(self.__a)
			raise Caps.IncorrectTypeException()
		
		def getDouble(self) -> float:
			"""Validate if value is float/DOUBLE and return it"""
			if self.type() == Caps.Value.TYPE_DOUBLE: return float(self.__a)
			raise Caps.IncorrectTypeException()
		
		def getString(self) -> str:
			"""Validate if value is str/STRING and return it"""
			if self.type() == Caps.Value.TYPE_STRING: return str(self.__a)
			raise Caps.IncorrectTypeException()
		
		def getBinary(self) -> bytes:
			"""Validate if value is bytes/BINARY and return it"""
			if self.type() == Caps.Value.TYPE_BINARY: return bytes(self.__a)
			raise Caps.IncorrectTypeException()
		
		def getObject(self) -> Caps:
			"""Validate if value is Caps/OBJECT and return it"""
			if self.type() == Caps.Value.TYPE_OBJECT: return self.__a
			raise Caps.IncorrectTypeException()

		def __repr__(self) -> str:
			current_type = self.type()
			a = [i for i in Caps.Value.__dict__.items() if i[1] == current_type]
			type_string = 'Caps.Value.' + a[0][0] if len(a) == 1 else current_type
			value_string = "'" + str(self.__a) + "'" if current_type == Caps.Value.TYPE_STRING else str(self.__a)
			return "Caps.Value(value=%s, vType=%s)" % (value_string, type_string)

# Example usage
if __name__ == "__main__":
	# Create a Caps object
	caps = Caps()
	caps.writeUInt32(42)
	caps.writeString("Hello, World!")
	caps.writeDouble(3.14159)
	
	# Nested Caps
	nested = Caps()
	nested.writeString("nested string")
	nested.writeUInt32(123)
	caps.writeObject(nested)
	
	# Serialize
	data = caps.serialize()
	print("Serialized data:", data)
	print("Size:", len(data), "bytes")
	
	# Deserialize
	parsed, _ = Caps.fromBytes(data)
	print("\nParsed:", parsed, "\n")
	print("Value 0:", parsed.at(0).getInt())
	print("Value 1:", parsed.at(1).getString())
	print("Value 2:", parsed.at(2).getDouble())
	print("Value 3 (nested):", parsed.at(3).getObject())
