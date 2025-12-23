from typing import Optional
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class FileData:
	absoluteFilePath: str
	createDate: int
	fileName: str
	fileSize: int
	modifiedDate: int
	webFilePath: str
	isDir: bool
	childList: Optional[list['FileData']] = None
	mimeType: Optional[str] = None
