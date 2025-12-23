class BatteryLevelUpdateListener:
	"""BatteryLevelUpdateListener Interface - Please extend this class and implement the methods"""
	def onBatteryLevelUpdated(self, level: int, isCharging: bool) -> None: pass
