class Clock():

	def __init__(self, hours, minutes=00):
		self.hours = hours
		self.minutes = minutes
	
	@classmethod
	def at(cls, hours, minutes=00):
		return cls(hours, minutes)
	
	def __str__(self):
		hour_time = self.hours
		minute_time = self.minutes
		
		string_hour = str(hour_time)
		string_minute = str(minute_time)
		
		if len(string_hour) == 1:
			string_hour = "0" + string_hour
		else:
			pass
		
		if len(string_minute) == 1:
			string_minute = ":0" + string_minute
		else:
			pass
			
		return string_hour + string_minute
		
	
Clock.at(8).__str__()
 	

