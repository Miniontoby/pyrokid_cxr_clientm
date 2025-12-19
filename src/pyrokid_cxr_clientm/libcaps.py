"""
com.rokid.cxr.client-m:1.0.4 - jni/arm64-v8a/libcaps.so library in Python

Caps class is THE way to decode and encode packets when communicating to the Rokid Glasses.

Everything is of course Pythonified, so doSomethingMethods are now do_something_methods
and stuff like ``caps.at(index)`` is now ``caps[index]``, ``caps.size()`` is now ``len(caps)``
"""

import struct
import io
from typing import Any, List, Optional, Union, BinaryIO
from enum import IntEnum

class MemberType(IntEnum):
	"""DWARF-style type codes used in :type:`Caps` serialization"""
	VOID = ord('V')  # 0x56
	INT32 = ord('i')  # 0x69
	UINT32 = ord('u')  # 0x75
	FLOAT = ord('f')  # 0x66
	INT64 = ord('l')  # 0x6c
	UINT64 = ord('k')  # 0x6b
	DOUBLE = ord('d')  # 0x64
	STRING = ord('S')  # 0x53
	BINARY = ord('B')  # 0x42
	OBJECT = ord('O')  # 0x4f

class CapsError(Exception):
	"""Base exception for :type:`Caps` operations"""
	pass

class IncorrectTypeException(RuntimeError):
	"""Exception that throws when Type of a :type:`CapsValue` is not what you were expecting"""
	pass

class CapsValue:
	"""Represents a single value in :type:`Caps` format"""
	
	def __init__(self, value: Any = None, type_hint: Optional[MemberType] = None):
		self.value = value
		self.type_hint = type_hint
		
	def get_type(self) -> MemberType:
		"""Determine the type code for this value"""
		if self.type_hint:
			if isinstance(self.type_hint, MemberType):
				return self.type_hint
			return MemberType(self.type_hint)
			
		if self.value is None:
			return MemberType.VOID
		elif isinstance(self.value, bool):
			return MemberType.UINT32
		elif isinstance(self.value, int):
			if -2**31 <= self.value < 2**31:
				return MemberType.INT32
			elif 0 <= self.value < 2**32:
				return MemberType.UINT32
			elif -2**63 <= self.value < 2**63:
				return MemberType.INT64
			else:
				return MemberType.UINT64
		elif isinstance(self.value, float):
			return MemberType.FLOAT # Or double
		elif isinstance(self.value, str):
			return MemberType.STRING
		elif isinstance(self.value, (bytes, bytearray)):
			return MemberType.BINARY
		elif isinstance(self.value, Caps):
			return MemberType.OBJECT
		else:
			raise CapsError("Unsupported type: %s" % (type(self.value)))

	def __repr__(self) -> str:
		current_type = self.get_type()
		value_string = "'" + str(self.value) + "'" if current_type == MemberType.STRING else str(self.value)
		return "CapsValue(value=%s, type_hint=MemberType.%s)" % (value_string, current_type.name)

	def get_int(self) -> int:
		"""Validate if value is int/IN32/UINT32 and return it"""
		if self.get_type() == MemberType.INT32 or self.get_type() == MemberType.UINT32: return self.value
		raise IncorrectTypeException()
    
	def get_long(self) -> int:
		"""Validate if value is long/INT64/UINT64 and return it"""
		if self.get_type() == MemberType.INT64 or self.get_type() == MemberType.UINT64: return self.value
		raise IncorrectTypeException()
	    
	def get_float(self) -> float:
		"""Validate if value is float/FLOAT and return it"""
		if self.get_type() == MemberType.FLOAT: return self.value
		raise IncorrectTypeException()
	    
	def get_double(self) -> float:
		"""Validate if value is float/DOUBLE and return it"""
		if self.get_type() == MemberType.DOUBLE: return self.value
		raise IncorrectTypeException()
	    
	def get_string(self) -> str:
		"""Validate if value is str/STRING and return it"""
		if self.get_type() == MemberType.STRING: return self.value
		raise IncorrectTypeException()
	    
	def get_binary(self) -> bytes:
		"""Validate if value is bytes/BINARY and return it"""
		if self.get_type() == MemberType.BINARY: return self.value
		raise IncorrectTypeException()
	    
	def get_object(self) -> 'Caps':
		"""Validate if value is Caps/OBJECT and return it"""
		if self.get_type() == MemberType.OBJECT: return self.value
		raise IncorrectTypeException()

class Caps:
	"""Main Caps container class for serialization/deserialization

	:param Optional[List[CapsValue]] values: Optional values list, in case you already have a list of :type:`CapsValue`'s.
		Else its recommended to use :func:`Caps.from_bytes`
	"""
	
	CAPS_VERSION = 5
	"""Current Caps version."""

	members: List[CapsValue]
	"""The :type:`CapsValue` members of this Caps object."""
	
	def __init__(self, values: Optional[List[CapsValue]] = None):
		self.members: List[CapsValue] = values or []
	
	def write(self, value: Any = None) -> 'Caps':
		"""Add a value to the Caps object"""
		if isinstance(value, CapsValue):
			self.members.append(value)
		else:
			self.members.append(CapsValue(value))
		return self
	
	def write_int(self, value: int) -> 'Caps':
		"""Write an integer value"""
		return self.write(CapsValue(value, MemberType.INT32))
	
	def write_uint(self, value: int) -> 'Caps':
		"""Write an unsigned integer value"""
		return self.write(CapsValue(value, MemberType.UINT32))
	
	def write_long(self, value: int) -> 'Caps':
		"""Write a long integer value"""
		return self.write(CapsValue(value, MemberType.INT64))
	
	def write_ulong(self, value: int) -> 'Caps':
		"""Write an unsigned long value"""
		return self.write(CapsValue(value, MemberType.UINT64))
	
	def write_float(self, value: float) -> 'Caps':
		"""Write a float value"""
		return self.write(CapsValue(value, MemberType.FLOAT))
	
	def write_double(self, value: float) -> 'Caps':
		"""Write a double value"""
		return self.write(CapsValue(value, MemberType.DOUBLE))
	
	def write_string(self, value: str) -> 'Caps':
		"""Write a string value"""
		return self.write(CapsValue(value, MemberType.STRING))
	
	def write_binary(self, data: bytes) -> 'Caps':
		"""Write binary data"""
		return self.write(CapsValue(data, MemberType.BINARY))
	
	def write_object(self, caps: 'Caps') -> 'Caps':
		"""Write a nested :type:`Caps` object"""
		return self.write(CapsValue(caps, MemberType.OBJECT))
	
	def empty(self) -> bool:
		"""Check if Caps is empty"""
		return len(self.members) == 0
	
	def clear(self) -> None:
		"""Clear all members"""
		self.members.clear()
	
	def serialize(self) -> bytes:
		"""
		Serialize the Caps object to bytes
		Format: [4 bytes size][1 byte version][member descriptors][member data]
		"""
		# First pass: serialize member descriptors and data
		desc_buffer = io.BytesIO()
		data_buffer = io.BytesIO()
		
		# Write member count as ULEB128
		desc_buffer.write(self._encode_uleb128(len(self.members)))
		
		# Write type descriptors
		for member in self.members:
			if not isinstance(member, CapsValue): continue
			member_type = member.get_type()
			desc_buffer.write(bytes([member_type]))
		
		# Write member data
		for member in self.members:
			if not isinstance(member, CapsValue): continue
			self._serialize_member(member, data_buffer)
		
		# Combine everything
		desc_data = desc_buffer.getvalue()
		member_data = data_buffer.getvalue()
		
		total_size = 5 + len(desc_data) + len(member_data)
		
		result = io.BytesIO()
		result.write(struct.pack('>I', total_size))  # Big-endian size
		result.write(bytes([self.CAPS_VERSION]))
		result.write(desc_data)
		result.write(member_data)
		
		return result.getvalue()
	
	def _serialize_member(self, member: CapsValue, buffer: BinaryIO) -> None:
		"""Serialize a single member's data"""
		member_type = member.get_type()
		value = member.value
		
		if member_type == MemberType.VOID:
			pass  # No data
		elif member_type == MemberType.INT32:
			buffer.write(self._encode_sleb128(value))
		elif member_type == MemberType.UINT32:
			buffer.write(self._encode_uleb128(value))
		elif member_type == MemberType.FLOAT:
			buffer.write(struct.pack('<f', value))
		elif member_type == MemberType.INT64:
			buffer.write(self._encode_sleb128(value))
		elif member_type == MemberType.UINT64:
			buffer.write(self._encode_uleb128(value))
		elif member_type == MemberType.DOUBLE:
			buffer.write(struct.pack('<d', value))
		elif member_type == MemberType.STRING:
			encoded = value.encode('utf-8')
			buffer.write(self._encode_uleb128(len(encoded)))
			buffer.write(encoded)
		elif member_type == MemberType.BINARY:
			buffer.write(self._encode_uleb128(len(value)))
			buffer.write(value)
		elif member_type == MemberType.OBJECT:
			nested_data = value.serialize()
			buffer.write(nested_data)
		else:
			raise CapsError("Unknown member type: %d" % (member_type))
	
	def parse(self, data: bytes) -> 'Caps':
		"""Parse a bytes to the current Caps object"""
		if len(data) < 5:
			raise CapsError("Data too small")
			
		# Parse header
		size = struct.unpack('>I', data[0:4])[0]
		version = data[4]
		
		if version != Caps.CAPS_VERSION:
			raise CapsError("Unsupported version: %d" % (version))
		
		if size > len(data):
			raise CapsError("Size mismatch: expected %d, got %d" % (size, len(data)))
			
		# Parse members
		buffer = io.BytesIO(data[5:])
		
		# Read member count
		member_count, bytes_read = Caps._decode_uleb128(buffer)
		
		# Read type descriptors
		descriptors = []
		for _ in range(member_count):
			desc = buffer.read(1)
			if not desc:
				raise CapsError("Truncated descriptor data")
			descriptors.append(desc[0])
		
		# Read member data
		for desc in descriptors:
			descType = MemberType(desc)
			value = Caps._parse_member(descType, buffer)
			self.members.append(CapsValue(value, descType))
		
		return self
	
	@staticmethod
	def from_bytes(data: bytes) -> 'Caps':
		"""Parse a new Caps object from bytes"""
		caps = Caps()
		return caps.parse(data)
	
	@staticmethod
	def _parse_member(member_type: MemberType, buffer: BinaryIO) -> Any:
		"""Parse a single member from the buffer"""
		if member_type == MemberType.VOID:
			return None
		elif member_type == MemberType.INT32:
			value, _ = Caps._decode_sleb128(buffer)
			return value
		elif member_type == MemberType.UINT32:
			value, _ = Caps._decode_uleb128(buffer)
			return value
		elif member_type == MemberType.FLOAT:
			data = buffer.read(4)
			return struct.unpack('<f', data)[0]
		elif member_type == MemberType.INT64:
			value, _ = Caps._decode_sleb128(buffer)
			return value
		elif member_type == MemberType.UINT64:
			value, _ = Caps._decode_uleb128(buffer)
			return value
		elif member_type == MemberType.DOUBLE:
			data = buffer.read(8)
			return struct.unpack('<d', data)[0]
		elif member_type == MemberType.STRING:
			length, _ = Caps._decode_uleb128(buffer)
			data = buffer.read(length)
			return data.decode('utf-8')
		elif member_type == MemberType.BINARY:
			length, _ = Caps._decode_uleb128(buffer)
			return buffer.read(length)
		elif member_type == MemberType.OBJECT:
			# Read size header
			size_data = buffer.read(4)
			size = struct.unpack('>I', size_data)[0]
			# Read rest of caps data
			caps_data = size_data + buffer.read(size - 4)
			return Caps.from_bytes(caps_data)
		else:
			raise CapsError("Unknown member type: %d" % (member_type))
	
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
	def _decode_uleb128(buffer: BinaryIO) -> tuple[int, int]:
		"""Decode ULEB128 from buffer, returns (value, bytes_read)"""
		result = 0
		shift = 0
		bytes_read = 0
		
		while True:
			byte_data = buffer.read(1)
			if not byte_data:
				raise CapsError("Truncated ULEB128")
			byte = byte_data[0]
			bytes_read += 1
			
			result |= (byte & 0x7F) << shift
			shift += 7
			
			if (byte & 0x80) == 0:
				break
				
			if shift >= 64:
				raise CapsError("ULEB128 too large")
				
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
	def _decode_sleb128(buffer: BinaryIO) -> tuple[int, int]:
		"""Decode SLEB128 from buffer, returns (value, bytes_read)"""
		result = 0
		shift = 0
		bytes_read = 0
		byte = 0x80
		
		while (byte & 0x80) != 0:
			byte_data = buffer.read(1)
			if not byte_data:
				raise CapsError("Truncated SLEB128")
			byte = byte_data[0]
			bytes_read += 1
			
			result |= (byte & 0x7F) << shift
			shift += 7
			
		# Sign extend
		if shift < 64 and (byte & 0x40) != 0:
			result |= -(1 << shift)
			
		return result, bytes_read
	
	def __getitem__(self, index: int) -> CapsValue:
		"""Get member value by index"""
		if index < 0 or index >= len(self.members):
			raise IndexError("Index out of range")
		return self.members[index]
	
	def __len__(self) -> int:
		"""Return the number of members"""
		return len(self.members)
	
	def __repr__(self) -> str:
		return "Caps(%s)" % self.members


# Example usage
if __name__ == "__main__":
	# Create a Caps object
	caps = Caps()
	caps.write_int(42)
	caps.write_string("Hello, World!")
	caps.write_double(3.14159)
	
	# Nested Caps
	nested = Caps()
	nested.write_string("nested string")
	nested.write_int(123)
	caps.write_caps(nested)
	
	# Serialize
	data = caps.serialize()
	print("Serialized data:", data)
	print("Size:", len(data), "bytes")
	
	# Deserialize
	parsed = Caps.from_bytes(data)
	print("\nParsed:", parsed, "\n")
	print("Value 0:", parsed[0].value)
	print("Value 1:", parsed[1].value)
	print("Value 2:", parsed[2].value)
	print("Value 3 (nested):", parsed[3].value)
