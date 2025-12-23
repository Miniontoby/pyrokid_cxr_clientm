from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class BaseNetworkResponse:
	errorCode: int = 200
	errorMsg: str = ''
	isSuccess: bool = False
