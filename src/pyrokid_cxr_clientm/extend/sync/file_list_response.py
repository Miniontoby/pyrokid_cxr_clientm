"""
com.rokid.cxr.client-m:1.0.4 - extend/sync/FileListResponse.java in Python

FileListResponse class is the JSON model for the http filelist responses
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .base_network_response import BaseNetworkResponse
from .file_data import FileData

@dataclass_json
@dataclass
class FileListResponse(BaseNetworkResponse):
	"""com.rokid.cxr.client.extend.sync.FileListResponse Java class to Python"""
	data: list[FileData] = None
