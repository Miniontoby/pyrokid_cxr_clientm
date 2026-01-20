"""com.rokid.cxr.client-m:1.0.4 - extend/listeners/BatteryLevelUpdateListener.java in Python"""

from abc import ABC, abstractmethod

class BatteryLevelUpdateListener(ABC):
	"""com.rokid.cxr.client.extend.listeners.BatteryLevelUpdateListener Java interface to Python - Please extend this class and implement the methods"""
	@abstractmethod
	def onBatteryLevelUpdated(self, level: int, isCharging: bool) -> None: pass
