from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .base_network_response import BaseNetworkResponse
from .file_data import FileData

@dataclass_json
@dataclass
class FileListResponse(BaseNetworkResponse):
	data: list[FileData] = None
