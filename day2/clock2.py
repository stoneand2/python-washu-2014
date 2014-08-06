class Clock():

	def __init__(self, hours, minutes=00):
		self.hours = hours # this is an instance variable, able to be accessed anywhere you call self
		self.minutes = minutes
		
	
	@classmethod #instead of self, the first thing we access is the class itself
	def at(cls, hours, minutes=00):
		return cls(hours, minutes) # basically, same as return Clock(...)		
		
	def __add__(self, number):
	
		
		hour_time = self.hours
		minute_time = self.minutes
		
		if number + minute_time < 60:
			minute_time = minute_time + number
		elif number + minute_time > 60:
			minute_time = (number + minute_time) - 60 #### won't work if over 120
			hour_time = hour_time + ((number + minute_time) / 60)
		else:
			pass
		
		if hour_time > 23:
			hour_time = (hour_time) - 24
		else:
			pass
		
		self.hours = hour_time
		
		self.minutes = minute_time
		return self # lets you use self.hours and self.minutes in the __str__ method
		
	def __str__(self):	
	
		hour_time2 = self.hours
		minute_time2 = self.minutes


		string_hour = str(hour_time2)
		string_minute = str(minute_time2)
		
		if len(string_hour) == 1:
			string_hour = "0" + string_hour
		else:
			pass
		
		if len(string_minute) == 1:
			string_minute = ":0" + string_minute
		else:
			pass
			
		return string_hour + string_minute
		
clock = Clock.at(23) + 3
print clock.__str__()