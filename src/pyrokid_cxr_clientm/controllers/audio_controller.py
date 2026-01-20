"""
com.rokid.cxr.client-m:1.0.4 - controllers/AudioController in Python

AudioController class allowed the mobile app to set communication device.
For Python its basically useless.
"""

from __future__ import annotations
from ..utils import LogUtil

class AudioController:
	"""com.rokid.cxr.client.controllers.AudioController Java class in Python"""
	a = None # AudioManager
	"""mAudioManager"""

	def __init__(self):
		LogUtil.i("AudioController", "AudioController constructed")
	
	@staticmethod
	def getInstance() -> AudioController:
		LogUtil.v("AudioController", "getInstance")
		return _a.a
	
	def setCommunicationDevice(self, context) -> None:
		LogUtil.i("AudioController", "setCommunicationDevice")
		return None
		#self.a = context.getSystemService("audio") # AudioManager
		self.a = None
		LogUtil.i("AudioController", "mAudioManager: %s", self.a)
		audioManager: AudioManager = this.a
		if audioManager is not None:
			#if Build.VERSION.SDK_INT < 31:
			#	LogUtil.i("AudioController", "isBluetoothScoOn: %s", self.a.isBluetoothScoOn())
			#	self.a.setBluetoothScoOn(True)
			#	self.a.startBluetoothSco()
			#	return
			for audioDeviceInfo in audioManager.getDevices(2):
				if audioDeviceInfo.getType() == 7:
					LogUtil.i("AudioController", "product name: %s", audioDeviceInfo.getProductName())
					self.a.setCommunicationDevice(audioDeviceInfo)
					return
	
	def clearCommunicationDevice(self) -> None:
		LogUtil.i("AudioController", "clearCommunicationDevice")
		return None
		LogUtil.i("AudioController", "mAudioManager: %s", self.a)
		audioManager: AudioManager = self.a
		if audioManager is not None:
			#if Build.VERSION.SDK_INT >= 31:
			#	audioManager.clearCommunicationDevice()
			#else:
			if False:
				LogUtil.i("AudioController", "isBluetoothScoOn: %s", self.a.isBluetoothScoOn())
				self.a.setBluetoothScoOn(False)
				self.a.stopBluetoothSco()
			self.a = None

class _a: a = AudioController()

__all__ = ['AudioController']
