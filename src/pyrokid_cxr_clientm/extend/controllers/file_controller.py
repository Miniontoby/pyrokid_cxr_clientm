from __future__ import annotations
from typing import Callable
from requests import Response
from threading import Thread
import os
from ..callbacks import ApkStatusCallback
from ...utils import LogUtil, ValueUtil
from ..sync.file_data import FileData
from ..sync.file_list_response import FileListResponse
from ..sync.retrofit_client import RetrofitClient

class FileController:
	t = ["/storage/emulated/0/Recordings", "/storage/emulated/0/DCIM/Camera", "/storage/emulated/0/Movies/Camera"]
	a = None # Context
	b: str
	c: list[str]
	d: str = None
	e: bool
	f: FileController.Callback = None
	g: int
	h: bool = False
	i = None # All of these are Classes from RetrofitClient's Service
	j: bool = False
	k = None
	l: bool = False
	m = None
	n: bool = False
	o = None
	p: bool = False
	q: ApkStatusCallback = None
	r = None
	s: bool = False

	@staticmethod
	def getInstance() -> FileController:
		LogUtil.v("FileController", "getInstance")
		return _d.a

	@staticmethod
	def deleteFile(paramFileController: FileController, paramString: str) -> None:
		LogUtil.i("FileController", "deleteFile")
		requestBody = RetrofitClient.createPartFromString(paramString)
		LogUtil.i("FileController", "deleteFile requestBody: %s", requestBody)
		paramFileController.o = RetrofitClient.getInstance().getService().deleteFile(requestBody)
		LogUtil.i("FileController", "mDeleteFileCall: %s", paramFileController.o)
		paramFileController.p = True
		paramFileController.o.enqueue(_mDeleteFileCall(paramFileController))

	def startUploadApk(self, paramFile, paramString: str, paramApkStatusCallback: ApkStatusCallback) -> None:
		LogUtil.i("FileController", "startUploadApk")
		self.q = paramApkStatusCallback
		RetrofitClient.getInstance().setBaseUrl("http://" + paramString + ":8848")
		requestBody = RetrofitClient.createPartFromApk(paramFile)
		LogUtil.i("FileController", "startUploadApk requestBody: %s", requestBody)
		self.r = RetrofitClient.getInstance().getService().uploadFile(("upfile", paramFile, "application/vnd.android.package-archive"))
		LogUtil.i("FileController", "mUploadApkCall: %s", self.r)
		self.s = True
		self.r.enqueue(_mUploadApkCall(self))

	@staticmethod
	def downloadFile(paramFileController: FileController, fileList: list[FileData], fileIndex: int):
		LogUtil.i("FileController", "downloadFile fileIndex: %d, mNeedDownload: %d", fileIndex, paramFileController.h);
		if paramFileController.h:
			if fileIndex >= len(fileList):
				paramFileController.downloadMedia()
			else:
				fileData = fileList[fileIndex]
				savePath = paramFileController.b + fileData.fileName
				absoluteFilePath = fileData.absoluteFilePath
				requestBody = RetrofitClient.createPartFromString(absoluteFilePath)
				LogUtil.i("FileController", "downloadFile requestBody: %s", requestBody)
				paramFileController.k = RetrofitClient.getInstance().getService().downloadFile(requestBody)
				LogUtil.i("FileController", "mDownloadFileCall: %s", paramFileController.k)
				paramFileController.l = True
				paramFileController.k.enqueue(_mDownloadFileCall(paramFileController, absoluteFilePath, savePath, fileData, fileList, fileIndex))

	def downloadMedia(self):
		self.g += 1
		LogUtil.i("FileController", "downloadMedia mMediaIndex: %d, mNeedDownload: %d", self.g, self.h)
		if self.h is None:
			return
		if self.g < len(self.c):
			LogUtil.i("FileController", "fetchFileList")
			requestBody = RetrofitClient.createPartFromString(self.c[self.g])
			LogUtil.i("FileController", "fetchFileList requestBody: %s", requestBody)
			self.i = RetrofitClient.getInstance().getService().getFileList(requestBody)
			LogUtil.i("FileController", "mFetchFileListCall: %s", self.i)
			self.j = True
			self.i.enqueue(_mFetchFileListCall(self))
		else:
			callback = self.f
			if callback is not None:
				callback.onDownloadFinished()
			else:
				LogUtil.e("FileController", "mCallback is null")

	def reportDownload(self, paramString: str):
		LogUtil.i("FileController", "reportDownload")
		requestBody = RetrofitClient.createPartFromString(paramString)
		LogUtil.i("FileController", "reportDownload requestBody: %s", requestBody)
		self.m = RetrofitClient.getInstance().getService().reportDownload(requestBody)
		LogUtil.i("FileController", "mReportDownloadCall: %s", self.m)
		self.n = True
		self.m.enqueue(_mReportDownloadCall(self, paramString))

	def __init__(self):
		LogUtil.i("FileController", "FileController constructed")

	@staticmethod
	def generateMediaPaths(paramArrayOfCxrMediaType: list[ValueUtil.CxrMediaType]) -> list[str]:
		LogUtil.i("FileController", "generateMediaPaths")
		arrayList = []
		i = False
		j = len(paramArrayOfCxrMediaType)
		for mediaType in paramArrayOfCxrMediaType:
			LogUtil.i("FileController", "check has all: %s", mediaType)
			if mediaType == ValueUtil.CxrMediaType.ALL:
				i = True
				break
		if i == True:
			for strValue in FileController.t: arrayList.append(strValue)
		else:
			for strValue in paramArrayOfCxrMediaType:
				LogUtil.i("FileController", "iterate type list: %s", strValue);
				k = strValue.value
				if k != 0:
					if k != 1:
						if k == 2: arrayList.append(FileController.t[2])
					else:
						arrayList.append(FileController.t[1])
				else:
					arrayList.append(FileController.t[0])
		return arrayList

	def startDownload(self, paramContext, savePath: str, types: list[ValueUtil.CxrMediaType], fileToDownload: str, ipAddress: str, paramCallback: FileController.Callback) -> None:
		LogUtil.i("FileController", "startDownload")
		if savePath is not None and not len(savePath.strip()) == 0 and not savePath.endswith('/'):
			savePath += '/' # Added by me
		self.a = paramContext
		self.b = savePath
		self.c = FileController.generateMediaPaths(types)
		self.d = fileToDownload
		self.e = False
		self.f = paramCallback
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
	
	def stopUploadApk(self) -> None:
		LogUtil.i("FileController", "stopUploadApk")
		if self.r is not None and self.s:
			LogUtil.i("FileController", "cancel mUploadApkCall")
			self.r.cancel()
		self.q = None

	class Callback:
		"""FileController.Callback Interface - """
		def onDownloadStart(self) -> None: pass
		def onSingleFileDownloaded(self, param1String: str) -> None: pass
		def onDownloadFailed(self) -> None: pass
		def onDownloadFinished(self) -> None: pass

class _mDeleteFileCall: # retrofit2.Callback<ResponseBody>
	def __init__(self, this: FileController): self.a = this
	def onResponse(self, paramCall, responseBody: Response):
		self.a.p = False
		responseBody = BaseNetworkResponse.from_json(param1Response.text)
		LogUtil.i("FileController", "mDeleteFileCall onResponse result: %s, body: %s, code: %d", param1Response.ok, responseBody, param1Response.status_code)
		if not param1Response.ok:
			LogUtil.e("FileController", "mDeleteFileCall errorBody: %s" + responseBody.errorMsg);
	def onFailure(self, paramCall, paramThrowable: Exception):
		LogUtil.e("FileController", "mDeleteFileCall onFailure message: %s", paramThrowable)
		self.a.p = False

class _mUploadApkCall: # retrofit2.Callback<ResponseBody>
	def __init__(self, this: FileController): self.a = this
	def onResponse(self, param1Call, responseBody):
		apkStatusCallback = self.a.q
		self.a.s = False
		LogUtil.i("FileController", "mUploadApkCall onResponse result: %s", responseBody)
		if responseBody.isSuccess:
			LogUtil.i("FileController", "mUploadApkCall succeed")
			if apkStatusCallback is not None:
				apkStatusCallback.onUploadApkSucceed()
				return
		else:
			LogUtil.e("FileController", "mUploadApkCall errorBody: %s", responseBody.errorMsg)
			if apkStatusCallback is not None:
				apkStatusCallback.onUploadApkFailed()
				return
		LogUtil.e("FileController", "mApkStatusCallback is null")
	def onFailure(self, param1Call, param1Throwable: Exception):
		LogUtil.e("FileController", "mUploadApkCall onFailure message: %s", param1Throwable)
		self.a.s = False
		apkStatusCallback = self.a.q
		if apkStatusCallback is not None:
			apkStatusCallback.onUploadApkFailed()
		else:
			LogUtil.e("FileController", "mApkStatusCallback is null")

class _mDownloadFileCall:
	def __init__(self, this: FileController, absoluteFilePath: str, savePath: str, paramFileData: FileData, fileList: list[FileData], fileIndex: int):
		self.f = this
		self.e = absoluteFilePath
		self.d = savePath
		self.c = paramFileData
		self.b = fileList
		self.a = fileIndex
	def onResponse(self, paramCall, param1Response: Response):
		self.f.l = False
		responseBody = param1Response
		LogUtil.i("FileController", "mDownloadFileCall onResponse result: %s, body: [to big], code: %d", param1Response.ok, param1Response.status_code)
		if param1Response.ok and responseBody is not None:
			a1 = _mDownloadFileCall.a(self, responseBody)
			Thread(target=a1.run, daemon=True).start()
		else:
			LogUtil.e("FileController", "mDownloadFileCall errorBody: ", responseBody.errorMsg)
			self.f.reportDownload(self.a)
			callback = self.f.f
			if callback is not None:
				callback.onDownloadFailed()
			else:
				LogUtil.e("FileController", "mCallback is null")
	def onFailure(self, paramCall, paramThrowable: Exception):
		LogUtil.e("FileController", paramThrowable)
		LogUtil.e("FileController", "mDownloadFileCall onFailure message: %s", paramThrowable)
		self.f.l = False
		callback = self.f.f
		if callback is not None:
			callback.onDownloadFailed()
		else:
			LogUtil.e("FileController", "mCallback is null")
	class a: # Runnable
		def __init__(self, this: 'mDownloadFileCall', param1ResponseBody):
			self.b = this
			self.a = param1ResponseBody
		def run(self) -> None:
			fileController: FileController = self.b.f
			str1: str = self.b.e
			str2: str = self.b.d
			fileData: FileData = self.b.c
			createDate: int = fileData.createDate
			LogUtil.i("FileController", "cxr-- saveFile mNeedDownload: %s, len: %s", fileController.h, self.a.headers.get('content-length'))
			if not fileController.h:
				LogUtil.i("FileController", str1)
				if fileController.d is not None:
					FileController.downloadFile(fileController, self.b.d, self.b.e + 1)
					return
				else:
					LogUtil.i("FileController", "mFilePath is nonnull");
					FileController.downloadMedia()
					return
			try:
				if os.path.exists(str2):
					LogUtil.w("FileController", "file existed %s", str2)
					#os.unlink(str2)
					#LogUtil.i("FileController", "file delete result: %s", delete)
				else:
					LogUtil.w("FileController", "file not existed %s", str2)
				with open(str2, 'wb') as f:
					for chunk in self.a.iter_content(chunk_size=8192):
						if not fileController.h:
							break
						f.write(chunk)
				if fileController.h:
					os.utime(str2, (createDate / 1000, createDate / 1000))
					LogUtil.i("FileController", "saveFile succeed,savePath: %s", str2)
					'''
					Intent intent = new Intent("android.intent.action.MEDIA_SCANNER_SCAN_FILE")
					intent.setData(Uri.fromFile(file))
					fileController.a.sendBroadcast(intent)
					'''
					LogUtil.i("FileController", "sendBroadcast to scanning media file")
					callback: FileController.Callback = fileController.f
					if callback is not None:
						callback.onSingleFileDownloaded(str2)
					else:
						LogUtil.d("FileController", "mCallback is null")
				else:
					LogUtil.e("FileController", "saveFile stopped")
			except Exception as e:
				LogUtil.e("FileController", e)
			LogUtil.i("FileController", str1)
			listV = self.b.b
			if fileController.d is not None or True: # I added or True, cause with startSync it passes None but it doesnt seem like .d gets a value along the way...
				fileController.downloadFile(fileController, listV, self.b.a + 1)
			else:
				LogUtil.d("FileController", "mFilePath is null")
				fileController.f.onDownloadFailed()

class _mFetchFileListCall:
	def __init__(self, this: FileController): self.a = this
	def onResponse(self, paramCall, param1Response: Response):
		self.a.j = False
		fileListResponse = FileListResponse.from_json(param1Response.text)
		LogUtil.i("FileController", "mFetchFileListCall onResponse result: %s, body: %s, code: %d", param1Response.ok, fileListResponse, param1Response.status_code)
		callback = self.a.f
		if param1Response.ok and fileListResponse is not None and fileListResponse.isSuccess:
			listV = fileListResponse.data
			LogUtil.i("FileController", "cxr-- fileDataList: %d", len(listV))
			if len(listV) > 0:
				b1 = 0
				for fileData in listV:
					LogUtil.i("FileController", "%s", fileData.fileName)
					strValue = self.a.d
					if strValue is not None:
						if strValue == fileData.absoluteFilePath:
							self.a.e = True
							break
						b1 += 1
				if self.a.d is not None and not self.a.e and callback is not None:
					callback.onDownloadFailed()
					return
				LogUtil.i("FileController", "fileIndex: %d", b1)
				if self.a.g == 0 and callback is not None:
					callback.onDownloadStart()
				FileController.downloadFile(self.a, listV, b1)
			else:
				self.a.downloadMedia()
		else:
			LogUtil.e("FileController", "mFetchFileListCall failed")
			if callback is not None:
				callback.onDownloadFailed()
			else:
				LogUtil.e("FileController", "mCallback is null")
	def onFailure(self, paramCall, paramThrowable: Exception):
		LogUtil.e("FileController", "mFetchFileListCall onFailure message: %s", paramThrowable)
		self.a.j = False
		callback = self.a.f
		if callback is not None:
			callback.onDownloadFailed()
		else:
			LogUtil.e("FileController", "mCallback is null")

class _mReportDownloadCall: # retrofit2.Callback<ResponseBody>
	def __init__(self, this: FileController, param1String: str):
		self.a = param1String
		self.b = this
	def onResponse(self, param1Call, responseBody):
		self.b.n = False
		LogUtil.i("FileController", "mReportDownloadCall onResponse result: %s", responseBody)
		if not responseBody.isSuccess:
			LogUtil.e("FileController", "mReportDownloadCall errorBody: %s", responseBody.errorMsg)
		#FileController.deleteFile(self.b, self.a)
	def onFailure(self, param1Call, param1Throwable: Exception):
		LogUtil.e("FileController", "mReportDownloadCall onFailure message: %s", param1Throwable)
		self.b.n = False
		#FileController.deleteFile(self.b, self.a)


class _d: a: FileController = FileController()

