"""
com.rokid.cxr.client-m:1.0.4 - extend/sync/BaseNetworkRequest.java in Python

BaseNetworkRequest class is the JSON model for the http responses
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class BaseNetworkResponse:
	"""com.rokid.cxr.client.extend.sync.BaseNetworkResponse Java class to Python"""
	errorCode: int = 200
	errorMsg: str = ''
	isSuccess: bool = False
