"""
com.rokid.cxr.client-m:1.0.4 - extend/sync/FileData.java in Python

FileData class is the JSON model for the file data responses
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional

@dataclass_json
@dataclass
class FileData:
	"""com.rokid.cxr.client.extend.sync.FileData Java class to Python"""
	absoluteFilePath: str
	createDate: int
	fileName: str
	fileSize: int
	modifiedDate: int
	webFilePath: str
	isDir: bool
	childList: Optional[list['FileData']] = None
	mimeType: Optional[str] = None
