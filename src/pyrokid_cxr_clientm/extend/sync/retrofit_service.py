"""
com.rokid.cxr.client-m:1.0.4 - extend/sync/RetrofitService.java in Python

RetrofitService class is an attempt to recreate the code that Retrofit2 library would generate.
I know this looks ugly and stupid, but it kinda has to be.
"""

from requests import Session
from threading import Thread

class RetrofitService:
	def __init__(self, baseUrl: str, headers: dict[str, str]):
		self.baseUrl = baseUrl
		self.s = Session()
		self.s.headers = { **self.s.headers, **headers }

	def getFileList(self, filePath: str):
		'''
		@Multipart
		@POST("/server/openFileList")
		Call<FileListResponse> getFileList(@Part("filePath") RequestBody paramRequestBody);
		'''
		this = self
		# I know this looks stupid, but I want to stay as close to the original code as possible
		# And since these methods return a class with functions, I had to do this... I dont like it either
		class Call:
			t = None
			def enqueue(self, callback):
				self.t=Thread(target=self._run, args=[callback], daemon=True)
				self.t.start()
			def _run(self, callback):
				try:
					r = this.s.post(this.baseUrl + "/server/openFileList", data={'filePath': filePath})
					callback.onResponse(self, r)
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()

	def reportDownload(self, filePath: str):
		'''
		@Multipart
		@POST("/server/reportDownload")
		Call<ResponseBody> reportDownload(@Part("filePath") RequestBody paramRequestBody);
		'''
		this = self
		class Call:
			def enqueue(self, callback):
				try:
					r = this.s.post(this.baseUrl + "/server/reportDownload", data={'filePath': filePath})
					callback.onResponse(self, r)
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()

	def downloadFile(self, filePath: str):
		'''
		@Multipart
		@Streaming
		@POST("/server/downloadFile")
		Call<ResponseBody> downloadFile(@Part("filePath") RequestBody paramRequestBody);
		'''
		this = self
		class Call:
			t = None
			def enqueue(self, callback):
				self.t=Thread(target=self._run, args=[callback], daemon=True)
				self.t.start()
			def _run(self, callback):
				try:
					r = this.s.post(this.baseUrl + "/server/downloadFile", data={'filePath': filePath}, stream=True)
					callback.onResponse(self, r)
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				if self.t is not None:
					self.t.stop()
				return
		return Call()
	
	def deleteFile(self, filePath: str):
		'''
		@Multipart
		@POST("/server/deleteFile")
		Call<ResponseBody> deleteFile(@Part("filePath") RequestBody paramRequestBody);
		'''
		this = self
		class Call:
			t = None
			def enqueue(self, callback):
				self.t=Thread(target=self._run, args=[callback], daemon=True)
				self.t.start()
			def _run(self, callback):
				try:
					r = this.s.post(this.baseUrl + "/server/deleteFile", data={'filePath': filePath})
					callback.onResponse(self, r)
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()
	
	def uploadFile(self, paramPart: tuple[str, str, str]):
		'''
		@Multipart
		@POST("/server/upload")
		Call<ResponseBody> uploadFile(@Part MultipartBody.Part paramPart);
		'''
		(partName, filePath, dataType) = paramPart
		this = self
		class Call:
			t = None
			def enqueue(self, callback):
				self.t=Thread(target=self._run, args=[callback], daemon=True)
				self.t.start()
			def _run(self, callback):
				try:
					with open(filePath, 'rb') as f:
						files = {partName: (str(filePath).split('/')[-1], f, dataType)}
						r = this.s.post(this.baseUrl + "/server/upload", files=files)
						callback.onResponse(self, r)
				except Exception as exception:
					callback.onFailure(self, exception)
			def cancel(self):
				return
		return Call()
