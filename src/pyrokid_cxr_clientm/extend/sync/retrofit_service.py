from __future__ import annotations
from requests import Session, Response
from .base_network_response import BaseNetworkResponse
from .file_list_response import FileListResponse
from .header_interceptor import HeaderInterceptor

class RetrofitService:
	def __init__(self, baseUrl: str, headers):
		self.baseUrl = baseUrl
		self.s = Session()
		self.s.headers = { **self.s.headers, **headers }

	def getFileList(self, filePath: str) -> FileListResponse:
		'''
		@Multipart
		@POST("/server/openFileList")
		Call<FileListResponse> getFileList(@Part("filePath") RequestBody paramRequestBody);
		'''
		this = self
		# I know this looks stupid, but I want to stay as close to the original code as possible
		# And since these methods return a class with functions, I had to do this... I dont like it either
		class Call:
			def enqueue(self, callback):
				try:
					r = this.s.post(this.baseUrl + "/server/openFileList", data={'filePath': filePath})
					callback.onResponse(self, FileListResponse.from_json(r.text))
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()

	def reportDownload(self, filePath: str) -> Response:
		'''
		@Multipart
		@POST("/server/reportDownload")
		Call<ResponseBody> reportDownload(@Part("filePath") RequestBody paramRequestBody);
		'''
		this = self
		class Call:
			def enqueue(self, callback):
				try:
					r = self.s.post(self.baseUrl + "/server/reportDownload", data={'filePath': filePath})
					callback.onResponse(self, BaseNetworkResponse.from_json(r.text))
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()

	def downloadFile(self, filePath: str) -> Response:
		'''
		@Multipart
		@Streaming
		@POST("/server/downloadFile")
		Call<ResponseBody> downloadFile(@Part("filePath") RequestBody paramRequestBody);
		'''
		this = self
		class Call:
			def enqueue(self, callback):
				try:
					r = self.s.post(self.baseUrl + "/server/downloadFile", data={'filePath': filePath}, stream=True)
					callback.onResponse(self, BaseNetworkResponse.from_json(r.text))
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()
	
	def deleteFile(self, filePath: str) -> Response:
		'''
		@Multipart
		@POST("/server/deleteFile")
		Call<ResponseBody> deleteFile(@Part("filePath") RequestBody paramRequestBody);
		'''
		this = self
		class Call:
			def enqueue(self, callback):
				try:
					r = self.s.post(self.baseUrl + "/server/deleteFile", data={'filePath': filePath})
					callback.onResponse(self, BaseNetworkResponse.from_json(r.text))
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()
	
	def uploadFile(self, paramPart: tuple[str, str, str]) -> Response:
		'''
		@Multipart
		@POST("/server/upload")
		Call<ResponseBody> uploadFile(@Part MultipartBody.Part paramPart);
		'''
		(partName, filePath, dataType) = paramPart
		this = self
		class Call:
			def enqueue(self, callback):
				try:
					with open(filePath, 'rb') as f:
						files = {partName: (filePath.split('/')[-1], f, dataType)}
						r = self.s.post(self.baseUrl + "/server/upload", files=files)
						callback.onResponse(self, BaseNetworkResponse.from_json(r.text))
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()
