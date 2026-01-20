"""com.rokid.cxr.client-m:1.0.4 - extend/controllers/FileController.java in Python

FileController class handles the Wifi based File transfer.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable
from threading import Thread
import os
from requests import Response

from ..callbacks import ApkStatusCallback
from ...utils import LogUtil, ValueUtil
from ..sync.base_network_response import BaseNetworkResponse
from ..sync.file_data import FileData
from ..sync.file_list_response import FileListResponse
from ..sync.retrofit_client import RetrofitClient

class FileController:
	"""com.rokid.cxr.client.extend.controllers.FileController Java class in Python"""
	t = ["/storage/emulated/0/Recordings", "/storage/emulated/0/DCIM/Camera", "/storage/emulated/0/Movies/Camera"]
	a = None # Context
	"""mContext"""
	b: str
	"""savePath?"""
	c: list[str]
	"""filePathStringList"""
	d: str = None
	"""fileToDownload"""
	e: bool
	f: FileController.Callback = None
	"""mCallback"""
	g: int
	h: bool = False
	i = None
	"""mFetchFileListCall"""
	j: bool = False
	"""FetchFileList is running"""
	k = None
	"""mDownloadFileCall"""
	l: bool = False
	"""DownloadFile is running"""
	m = None
	"""mReportDownloadCall"""
	n: bool = False
	"""ReportDownload is running"""
	o = None
	"""mDeleteFileCall"""
	p: bool = False
	"""DeleteFile is running"""
	q: ApkStatusCallback = None
	r = None
	"""mUploadApkCall"""
	s: bool = False
	"""UploadApk is running"""
	autoDelete: bool = True

	class Callback(ABC):
		"""com.rokid.cxr.client.extend.controllers.FileController.Callback Interface - Please extend this class and implement the methods!"""
		@abstractmethod
		def onDownloadStart(self) -> None: pass
		@abstractmethod
		def onSingleFileDownloaded(self, fileName: str) -> None: pass
		@abstractmethod
		def onDownloadFailed(self) -> None: pass
		@abstractmethod
		def onDownloadFinished(self) -> None: pass

	def __init__(self):
		LogUtil.i("FileController", "FileController constructed")

	@staticmethod
	def getInstance() -> FileController:
		LogUtil.v("FileController", "getInstance")
		return _d.a

	@staticmethod
	def generateMediaPaths(cxrMediaTypeArr: list[ValueUtil.CxrMediaType]) -> list[str]:
		LogUtil.i("FileController", "generateMediaPaths")
		arrayList = []
		z = False
		for mediaType in cxrMediaTypeArr:
			LogUtil.i("FileController", "check has all: %s", mediaType)
			if mediaType == ValueUtil.CxrMediaType.ALL:
				z = True
				break
		if z == True:
			for strValue in FileController.t:
				arrayList.append(strValue)
		else:
			for cxrMediaType2 in cxrMediaTypeArr:
				LogUtil.i("FileController", "iterate type list: %s", cxrMediaType2)
				if cxrMediaType2 == ValueUtil.CxrMediaType.AUDIO:
					arrayList.append(FileController.t[0])
				elif cxrMediaType2 == ValueUtil.CxrMediaType.PICTURE:
					arrayList.append(FileController.t[1])
				elif cxrMediaType2 == ValueUtil.CxrMediaType.VIDEO:
					arrayList.append(FileController.t[2])					
		return arrayList

	@staticmethod
	def deleteFile(fileController: FileController, filePath: str) -> None:
		LogUtil.i("FileController", "deleteFile")
		requestBody = RetrofitClient.createPartFromString(filePath)
		LogUtil.i("FileController", "deleteFile requestBody: %s", requestBody)
		fileController.o = RetrofitClient.getInstance().getService().deleteFile(requestBody)
		LogUtil.i("FileController", "mDeleteFileCall: %s", fileController.o)
		fileController.p = True
		fileController.o.enqueue(_mDeleteFileCall(fileController))

	def startDownload(self, context, savePath: str, types: list[ValueUtil.CxrMediaType], fileToDownload: str, ipAddress: str, callback: FileController.Callback) -> None:
		LogUtil.i("FileController", "startDownload")
		if savePath is not None and not len(savePath.strip()) == 0 and not savePath.endswith('/'):
			savePath += '/' # Added by me
		self.a = context
		self.b = savePath
		self.c = FileController.generateMediaPaths(types)
		self.d = fileToDownload
		self.e = False
		self.f = callback
		self.g = -1
		self.h = True
		RetrofitClient.getInstance().setBaseUrl("http://" + ipAddress + ":8848")
		self.downloadMedia()

	def stopDownload(self) -> None:
		LogUtil.i("FileController", "stopDownload")
		self.h = False
		if self.i is not None and self.j:
			LogUtil.i("FileController", "cancel mFetchFileListCall")
			self.i.cancel()
		if self.k is not None and self.l:
			LogUtil.i("FileController", "cancel mDownloadFileCall")
			self.k.cancel()
		if self.m is not None and self.n:
			LogUtil.i("FileController", "cancel mReportDownloadCall")
			self.m.cancel()
		if self.o is not None and self.p:
			LogUtil.i("FileController", "cancel mDeleteFileCall")
			self.o.cancel()
		self.a = None
		self.b = None
		self.c = None
		self.d = None
		self.e = False
		self.f = None
		self.g = -1

	def startUploadApk(self, file, ipAddress: str, apkStatusCallback: ApkStatusCallback) -> None:
		LogUtil.i("FileController", "startUploadApk")
		self.q = apkStatusCallback
		RetrofitClient.getInstance().setBaseUrl("http://" + ipAddress + ":8848")
		requestBody = RetrofitClient.createPartFromApk(file)
		LogUtil.i("FileController", "startUploadApk requestBody: %s", requestBody)
		self.r = RetrofitClient.getInstance().getService().uploadFile(("upfile", file, "application/vnd.android.package-archive"))
		LogUtil.i("FileController", "mUploadApkCall: %s", self.r)
		self.s = True
		self.r.enqueue(_mUploadApkCall(self))

	def stopUploadApk(self) -> None:
		LogUtil.i("FileController", "stopUploadApk")
		if self.r is not None and self.s:
			LogUtil.i("FileController", "cancel mUploadApkCall")
			self.r.cancel()
		self.q = None

	@staticmethod
	def downloadFile(fileController: FileController, fileList: list[FileData], fileIndex: int):
		LogUtil.i("FileController", "downloadFile fileIndex: %d, mNeedDownload: %s", fileIndex, fileController.h)
		if fileController.h:
			if fileIndex >= len(fileList):
				fileController.downloadMedia()
				return
			fileData = fileList[fileIndex]
			absoluteFilePath = fileData.absoluteFilePath
			savePath = fileController.b + fileData.fileName
			requestBodyCreatePartFromString = RetrofitClient.createPartFromString(absoluteFilePath)
			LogUtil.i("FileController", "downloadFile requestBody: %s", requestBodyCreatePartFromString)
			fileController.k = RetrofitClient.getInstance().getService().downloadFile(requestBodyCreatePartFromString)
			LogUtil.i("FileController", "mDownloadFileCall: %s", fileController.k)
			fileController.l = True
			fileController.k.enqueue(_mDownloadFileCall(fileController, absoluteFilePath, savePath, fileData, fileList, fileIndex))

	def downloadMedia(self):
		self.g += 1
		LogUtil.i("FileController", "downloadMedia mMediaIndex: %d, mNeedDownload: %s", self.g, self.h)
		if self.h:
			if self.g < len(self.c):
				LogUtil.i("FileController", "fetchFileList")
				requestBodyCreatePartFromString = RetrofitClient.createPartFromString(self.c[self.g])
				LogUtil.i("FileController", "fetchFileList requestBody: %s", requestBodyCreatePartFromString)
				self.i = RetrofitClient.getInstance().getService().getFileList(requestBodyCreatePartFromString)
				LogUtil.i("FileController", "mFetchFileListCall: %s", self.i)
				self.j = True
				self.i.enqueue(_mFetchFileListCall(self))
				return
			callback: FileController.Callback = self.f
			if callback is not None:
				callback.onDownloadFinished()
			else:
				LogUtil.e("FileController", "mCallback is null")

	def reportDownload(self, filePath: str):
		LogUtil.i("FileController", "reportDownload")
		requestBodyCreatePartFromString = RetrofitClient.createPartFromString(filePath)
		LogUtil.i("FileController", "reportDownload requestBody: %s", requestBodyCreatePartFromString)
		self.m = RetrofitClient.getInstance().getService().reportDownload(requestBodyCreatePartFromString)
		LogUtil.i("FileController", "mReportDownloadCall: %s", self.m)
		self.n = True
		self.m.enqueue(_mReportDownloadCall(self, filePath))

class _mDeleteFileCall: # retrofit2.Callback<ResponseBody>
	def __init__(self, this: FileController): self.a = this

	def onResponse(self, call, response: Response):
		self.a.p = False
		zIsSuccessful = response.ok
		try: responseBody = BaseNetworkResponse.from_json(response.text)
		except: responseBody = None
		LogUtil.i("FileController", "mDeleteFileCall onResponse result: %s, body: %s, code: %d", zIsSuccessful, responseBody, response.status_code)
		if zIsSuccessful:
			if responseBody is not None:
				return
		LogUtil.e("FileController", "mDeleteFileCall errorBody: %s", response.text)
		
	def onFailure(self, call, th: Exception):
		LogUtil.e("FileController", "mDeleteFileCall onFailure message: %s", th)
		self.a.p = False

class _mUploadApkCall: # retrofit2.Callback<ResponseBody>
	def __init__(self, this: FileController): self.this = this

	def onResponse(self, call, response: Response):
		self.this.s = False
		zIsSuccessful = response.ok
		try: responseBody = BaseNetworkResponse.from_json(response.text)
		except: responseBody = None
		LogUtil.i("FileController", "mUploadApkCall onResponse result: %s, body: %s, code: %d", zIsSuccessful, responseBody, response.status_code)
		if zIsSuccessful:
			apkStatusCallback: ApkStatusCallback = self.this.q
			if responseBody is not None:
				LogUtil.i("FileController", "mUploadApkCall succeed")
				if apkStatusCallback is not None:
					apkStatusCallback.onUploadApkSucceed()
					return
			else:
				LogUtil.e("FileController", "mUploadApkCall errorBody: %s", response.text)
				if apkStatusCallback is not None:
					apkStatusCallback.onUploadApkFailed()
					return
		LogUtil.e("FileController", "mApkStatusCallback is null")

	def onFailure(self, call, th: Exception):
		LogUtil.e("FileController", "mUploadApkCall onFailure message: %s", th)
		fileController: FileController = self.this
		fileController.s = False
		apkStatusCallback: ApkStatusCallback = fileController.q
		if apkStatusCallback is not None:
			apkStatusCallback.onUploadApkFailed()
		else:
			LogUtil.e("FileController", "mApkStatusCallback is null")

class _mDownloadFileCall:
	a: str
	b: str
	c: FileData
	d: list[FileData]
	e: int
	f: FileController

	class a: # Runnable
		def __init__(self, this: '_mDownloadFileCall', responseBody):
			self.this = this
			self.a = responseBody

		def run(self) -> None:
			str1: str = None
			str2: str = None
			c0023a = self.this
			fileController: FileController = c0023a.f
			responseBody = self.a
			str3: str = c0023a.a
			str4: str = c0023a.b
			createDate: int = c0023a.c.createDate
			LogUtil.i("FileController", "cxr-- saveFile mNeedDownload: %s, len: %s", fileController.h, responseBody.headers.get('content-length'))
			if fileController.h:
				try:
					try:
						if os.path.exists(str4):
							LogUtil.w("FileController", "file existed %s", str4)
							#os.unlink(str4)
							#LogUtil.i("FileController", "file delete result: %s", delete)
						else:
							LogUtil.w("FileController", "file not existed %s", str4)
						try:
							with open(str4, 'wb') as f:
								for chunk in responseBody.iter_content(chunk_size=8192):
									if not fileController.h:
										break
									f.write(chunk)
						except Exception as e:
							LogUtil.e("FileController", e)
					except Exception as e:
						LogUtil.e("FileController", e)
					if fileController.h:
						os.utime(str4, (createDate / 1000, createDate / 1000))
						LogUtil.i("FileController", "saveFile succeed, savePath: %s", str4)
						callback: FileController.Callback = fileController.f
						if callback is not None:
							callback.onSingleFileDownloaded(str4)
							#fileController.reportDownload(str3)
						else:
							str1 = "FileController"
							str2 = "mCallback is null"
					else:
						str1 = "FileController"
						str2 = "saveFile stopped"
					if str1 is not None: LogUtil.e(str1, str2)
					fileController.reportDownload(str3)
				except Exception as e:
					LogUtil.e("FileController", e)
			c0023a = self.this
			fileController = c0023a.f
			if fileController.d is None:
				FileController.downloadFile(fileController, c0023a.d, c0023a.e + 1)
			else:
				LogUtil.i("FileController", "mFilePath is nonnull")
				self.this.f.downloadMedia()

	def __init__(self, this: FileController, absoluteFilePath: str, savePath: str, fileData: FileData, fileList: list[FileData], fileIndex: int):
		self.f = this
		self.a = absoluteFilePath
		self.b = savePath
		self.c = fileData
		self.d = fileList
		self.e = fileIndex

	def onResponse(self, call, response: Response):
		self.f.l = False
		zIsSuccessful = response.ok
		try: responseBody = response # must be
		except: responseBody = None
		LogUtil.i("FileController", "mDownloadFileCall onResponse result: %s, body: [to big], code: %d", zIsSuccessful, response.status_code)
		if zIsSuccessful:
			if responseBody is not None:
				a1 = _mDownloadFileCall.a(self, responseBody)
				Thread(target=a1.run, daemon=True).start()
				return
		LogUtil.e("FileController", "mDownloadFileCall errorBody: %s", response.text)
		self.f.reportDownload(self.a)
		callback: FileController.Callback = self.f.f
		if callback is not None:
			callback.onDownloadFailed()
		else:
			LogUtil.e("FileController", "mCallback is null")

	def onFailure(self, call, th: Exception):
		LogUtil.e("FileController", "mDownloadFileCall onFailure message: %s", th)
		fileController: FileController = self.f
		fileController.l = False
		callback: FileController.Callback = fileController.f
		if callback is not None:
			callback.onDownloadFailed()
		else:
			LogUtil.e("FileController", "mCallback is null")

class _mFetchFileListCall:
	def __init__(self, this: FileController): self.a = this

	def onResponse(self, call, response: Response):
		self.a.j = False
		zIsSuccessful = response.ok
		try: fileListResponse = FileListResponse.from_json(response.text)
		except: fileListResponse
		LogUtil.i("FileController", "mFetchFileListCall onResponse result: %s, body: %s, code: %d", zIsSuccessful, fileListResponse, response.status_code)
		callback: FileController.Callback = self.a.f
		if not zIsSuccessful or fileListResponse is None or not fileListResponse.isSuccess:
			LogUtil.m50e("FileController", "mFetchFileListCall failed")
			if callback is not None:
				callback.onDownloadFailed()
				return
			else:
				LogUtil.e("FileController", "mCallback is null")
				return
			
		data: list[FileData] = fileListResponse.data
		LogUtil.i("FileController", "cxr-- fileDataList: %d", len(data))
		if len(data) == 0:
			self.a.downloadMedia()
			return
		i = 0
		for fileData in data:
			LogUtil.i("FileController", "%s", fileData.fileName)
			strValue = self.a.d
			if strValue is not None:
				if strValue == fileData.absoluteFilePath or strValue == fileData.fileName:
					self.a.e = True
					break
				i += 1
		fileController: FileController = self.a
		callback = fileController.f
		if fileController.d is not None and not fileController.e and callback is not None:
			callback.onDownloadFailed()
			return
		LogUtil.i("FileController", "fileIndex: %d", i)
		if fileController.g == 0 and callback is not None:
			callback.onDownloadStart()
		FileController.downloadFile(self.a, data, i)

	def onFailure(self, call, th: Exception):
		LogUtil.e("FileController", "mFetchFileListCall onFailure message: %s", th)
		fileController: FileController = self.a
		fileController.j = False
		callback: FileController.Callback = fileController.f
		if callback is not None:
			callback.onDownloadFailed()
		else:
			LogUtil.e("FileController", "mCallback is null")

class _mReportDownloadCall: # retrofit2.Callback<ResponseBody>
	def __init__(self, this: FileController, filePath: str):
		self.a = filePath
		self.this = this

	def onResponse(self, call, response):
		self.this.n = False
		zIsSuccessful = response.ok
		try: responseBody = BaseNetworkResponse.from_json(response.text)
		except: responseBody = None
		LogUtil.i("FileController", "mReportDownloadCall onResponse result: %s, body: %s, code: %d", zIsSuccessful, responseBody, response.status_code)
		if zIsSuccessful:
			if responseBody is None:
				LogUtil.e("FileController", "mReportDownloadCall errorBody: %s", response.text)

		if self.a.endswith('-aiPic.jpg') or self.this.autoDelete:
			FileController.deleteFile(self.this, self.a)

	def onFailure(self, call, th: Exception):
		LogUtil.e("FileController", "mReportDownloadCall onFailure message: %s", th)
		fileController: FileController = self.this
		fileController.n = False
		if self.a.endswith('-aiPic.jpg') or self.this.autoDelete:
			FileController.deleteFile(fileController, self.a)


class _d: a: FileController = FileController()

