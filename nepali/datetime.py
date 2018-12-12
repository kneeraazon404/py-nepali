#
#
#	Author : Ajesh Sen Thapa
#	Website: www.ajesh.com.np
#
#

import time
import datetime

from .char import NepaliChar, EnglishChar


class NepaliDate:
	
	def __init__(self, npYear=0, npMonth=0, npDay=0):

		self.__enMonths = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
		self.enLeapMonths = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
		
		# List of np months
		self.__npMonths = [
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],	# 2000 BS - 1944 AD
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],	# 2001 BS
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],
			[ 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],	# 2071 BS
			[ 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],	# 2072 BS
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31 ],	# 2073 BS
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31 ],
			[ 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30 ],
			[ 31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30 ],
			[ 30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],	# 2090 BS
			[ 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30 ],
			[ 30, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 30, 30, 30, 30 ],
			[ 30, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30 ],
			[ 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30 ],
			[ 31, 31, 32, 31, 31, 31, 29, 30, 29, 30, 29, 31 ],
			[ 31, 31, 32, 31, 31, 31, 30, 29, 29, 30, 30, 30 ]	 # 2099 BS - 2042 AD
		]

		if npYear == 0 or npMonth == 0 or npDay == 0:
			self.setCurrentDate()
		else:
			self.setNpDate(npYear, npMonth, npDay)

	def __str__(self):
		return self.toNpString()

	def __repr__(self):
		return "<NepaliDate> "+str(self)

	def setCurrentDate(self):
		"""
		Setting current en date
		"""
		year = int(time.strftime("%Y"))
		month = int(time.strftime("%m"))
		date = int(time.strftime("%d"))
		self.setEnDate(year, month, date)

	
	#En to Np date conversion

	def setEnDate(self,year, month, date):
		"""
		* Sets specific en dates to self object *
		Refrence np 2000/1/1 with en date 1943/4/14
		"""
		if(not self.__isEnRange(year,month,date)):
			raise Exception("Invalid date format.")

		self.__enYear = year
		self.__enMonth = month
		self.__enDay = date

		# Setting np reference to 2000/1/1 with en date 1943/4/14
		self.__npYear = 2000
		self.__npMonth = 1
		self.__npDay = 1

		difference = self.enDateDifference(1943, 4, 14)

		# Getting np year untill the difference remains less than 365
		index = 0
		while( difference >= self.__npYearDays(index) ):
			self.__npYear+=1
			difference = difference - self.__npYearDays(index)
			index+=1

		# Getting np month untill the difference remains less than 31
		i = 0
		while(difference >= self.__npMonths[index][i]):
			difference = difference - self.__npMonths[index][i]
			self.__npMonth+=1
			i+=1

		# Remaning days is the date
		self.__npDay = self.__npDay + difference
		
		self.weekDay()
		

	def toEnString(self, format='-'):
		return str(self.__enYear)+format+str(self.__enMonth)+format+str(self.__enDay)
		

	def enDateDifference(self, year, month, date):
		"""
		returns difference of days from the self date with the date provided
		"""
		difference = self.__countTotalEnDays(self.__enYear, self.__enMonth, self.__enDay) - self.__countTotalEnDays(year, month, date)
		if difference < 0: 
			return -difference
		else:
			return difference
	

	def __countTotalEnDays(self, year, month, date):

		totalDays = year * 365 + date
				
		for i in range(0,month-1):
			totalDays = totalDays + self.__enMonths[i]
		
		totalDays = totalDays + self.__countleap(year, month)
		return totalDays


	def __countleap(self, year, month):
		if (month <= 2):
			year-=1
		
		return (year//4-year//100+year//400)
		

	def __isEnRange(self, year, month, date):
		
		if(year < 1944 or year > 2042):
			return False
		
		if(month < 1 or month > 12):
			return False
		
		if(date < 1 or date > 31):
			return False
		
		return True
	

	def __isLeapYear(self, year):

		if(year%4 == 0):
			if(year%100 == 0):
				return (year%400 == 0)
			else:
				return True								
		else:
			return False



	# Np to En date conversion

	def setNpDate(self, year, month, date):
		"""
		* Sets specific np dates to self object *
		Refrence en 1994/1/1 with en date 2000/9/17
		"""
		if(not self.__isNpRange(year,month,date)):
			raise Exception("Invalid date format.")

		self.__npYear = year
		self.__npMonth = month
		self.__npDay = date
		
		# Setting en reference to 1944/1/1 with np date 2000/9/17
		self.__enYear = 1944
		self.__enMonth = 1
		self.__enDay = 1
		
		difference = self.npDateDifference(2000, 9, 17)
		
		# Getting en year untill the difference remains less than 365
		while( (difference >= 366 and self.__isLeapYear(self.__enYear)) or	(difference >= 365 and not(self.__isLeapYear(self.__enYear)) ) ):
			if( self.__isLeapYear(self.__enYear) ):
				difference -= 366
			else:
				difference -= 365
			self.__enYear += 1
		
		# Getting en month untill the difference remains less than 31
		if(self.__isLeapYear(self.__enYear)):
			monthDays = self.enLeapMonths
		else: 
			monthDays = self.__enMonths
		i = 0
		while( difference >= monthDays[i]):
			self.__enMonth+=1
			difference = difference - monthDays[i]
			i+=1
		
		# Remaning days is the date
		self.__enDay = self.__enDay + difference
		
		self.weekDay()


	def toNpString(self, format="-"):
		return str(self.npYear())+format+str(self.npMonthStr())+format+str(self.npDayStr())

	
	def npDateDifference(self, year, month, date):

		# Getting difference from the current date with the date provided
		difference = self.__countTotalNpDays(self.__npYear, self.__npMonth, self.__npDay) - self.__countTotalNpDays(year, month, date)
		if(difference < 0):
			return -difference
		else:
			return difference


	def __countTotalNpDays(self, year, month, date):

		total = 0
		if(year < 2000):
			return 0
		
		total = total + (date-1)
		
		yearIndex = year - 2000
		for i in range(0,month-1):
			total = total + self.__npMonths[yearIndex][i]
		
		for i in range(0,yearIndex):
			total = total + self.__npYearDays(i)
		
		return total


	def __npYearDays(self, index):
		"""
		count total days of specific year ( from index)
		input: index (year)
		return total (days)
		"""
		total = 0
		
		for i in range(0,12):
			total += self.__npMonths[index][i]
		
		return total
		

	def __isNpRange(self, year, month, date):
		if(year < 2000 or year > 2098):
			return False
		
		if(month < 1 or month > 12):
			return False
		
		if(date < 1 or date > self.__npMonths[year-2000][month-1]):
			return False
		
		return True


	# Class Regular methods

	def weekDay(self):
		# Reference date 1943/4/14 Wednesday 
		difference = self.enDateDifference(1943, 4, 14)
		self.__week_day = ((3 + (difference%7) ) % 7 ) + 1
		return self.__week_day

	def enYear(self):
		return self.__enYear
	
	def enMonth(self):
		return self.__enMonth
	
	def enDay(self):
		return self.__enDay
	
	def npYear(self): 
		return self.__npYear
	
	def npMonth(self):
		return self.__npMonth
	
	def npDay(self):
		return self.__npDay

	def npMonthStr(self):
		npMonth = str(self.npMonth())
		if len(npMonth) < 2:
			npMonth = '0'+npMonth
		return npMonth

	def npDayStr(self):
		npDay = str(self.npDay())
		if len(npDay) < 2:
			npDay = '0'+npDay
		return npDay

	def to_date(self):
		return datetime.date(self.__enYear, self.__enMonth, self.__enDay)

	def to_date(self):
		return datetime.date(self.enYear(), self.enMonth(), self.enDay())

	def from_date(date_obj):
		npDate = NepaliDate()
		npDate.setEnDate(date_obj.year, date_obj.month, date_obj.day)
		return npDate

	def today():
		return NepaliDate()


	# property

	@property
	def year(self):
		return self.__npYear

	@property
	def month(self):
		return self.__npMonth

	@property
	def day(self):
		return self.__npDay

	@property
	def week_day(self):
		return self.weekDay()
	


class NepaliTime(datetime.time):

	def __repr__(self):
		return "<NepaliTime> "+str(self)


	# static methods

	def now(**kwargs):
		dt = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=45)
		if kwargs.get('microsecond'):
			return NepaliTime(dt.time().hour, dt.time().minute, dt.time().second, dt.time().microsecond)
		return NepaliTime(dt.time().hour, dt.time().minute, dt.time().second)


class NepaliDateTime:
	"""
	Nepali datetime
	"""

	def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0):
		self.__npDate = NepaliDate(year, month, day)
		self.__npTime = NepaliTime(hour, minute, second, microsecond) 

	def __str__(self):
		return str(self.__npDate)+' '+str(self.__npTime)

	def __repr__(self):
		return "<NepaliDateTime> "+str(self)

	# operator overloadings

	# addition
	def __add__(self, other):
		if type(other) == datetime.timedelta:
			"""
			timedelta object
			"""
			return NepaliDateTime.from_datetime(self.to_datetime() + other)
			pass

		return None

	# substraction
	def __sub__(self, other):
		if type(other) == self.__class__:
			"""
			NepaliDateTime object
			"""
			return self.to_datetime() - other.to_datetime()
			pass
		elif type(other) == datetime.datetime:
			return self.to_datetime() - other
			pass
		elif type(other) == datetime.timedelta:
			"""
			timedelta object
			"""
			return NepaliDateTime.from_datetime(self.to_datetime() - other)
			pass

		return None

	# less than
	def __lt__(self, other):
		if type(other) == self.__class__:
			"""
			NepaliDateTime object
			"""
			return self.to_datetime() < other.to_datetime()
			pass
		elif type(other) == datetime.datetime:
			"""
			datetime object
			"""
			return self.to_datetime() < other
			pass

		return None

	# less than euqal
	def __le__(self, other):
		if type(other) == self.__class__:
			"""
			NepaliDateTime object
			"""
			return self.to_datetime() <= other.to_datetime()
			pass
		elif type(other) == datetime.datetime:
			"""
			datetime object
			"""
			return self.to_datetime() <= other
			pass

		return None

	# equal
	def __eq__(self, other):
		if type(other) == self.__class__:
			"""
			NepaliDateTime object
			"""
			return self.to_datetime() == other.to_datetime()
			pass
		elif type(other) == datetime.datetime:
			"""
			datetime object
			"""
			return self.to_datetime() == other
			pass
			
		return None

	# not equal
	def __ne__(self, other):
		if type(other) == self.__class__:
			"""
			NepaliDateTime object
			"""
			return self.to_datetime() != other.to_datetime()
			pass
		elif type(other) == datetime.datetime:
			"""
			datetime object
			"""
			return self.to_datetime() != other
			pass
			
		return None
	
	# greater than
	def __gt__(self, other):
		if type(other) == self.__class__:
			"""
			NepaliDateTime object
			"""
			return self.to_datetime() > other.to_datetime()
			pass
		elif type(other) == datetime.datetime:
			"""
			datetime object
			"""
			return self.to_datetime() > other
			pass
			
		return None
	
	# greater than equal
	def __ge__(self, other):
		if type(other) == self.__class__:
			"""
			NepaliDateTime object
			"""
			return self.to_datetime() >= other.to_datetime()
			pass
		elif type(other) == datetime.datetime:
			"""
			datetime object
			"""
			return self.to_datetime() >= other
			pass
			
		return None 

	def to_datetime(self):
		return datetime.datetime.combine(self.__npDate.to_date(), self.__npTime)

	def date(self):
		return self.__npDate

	def time(self):
		return self.__npTime

	def strftime(self, format):
		formater = NepaliDateTimeFormater(self)
		return formater.get_str(format)

	def strftime_en(self, format):
		formater = NepaliDateTimeFormater(self, True)
		return formater.get_str(format)

	# static methods

	def from_datetime(dt, utc=False):
		if utc:
			dt = dt + datetime.timedelta(hours=5, minutes=45)	# +5:45 datetime
		nd = NepaliDate.from_date(dt.date())
		return NepaliDateTime(nd.npYear(), nd.npMonth(), nd.npDay(), dt.hour, dt.minute, dt.second)

	def now():
		return NepaliDateTime.from_datetime(datetime.datetime.utcnow(), True)


	# property

	@property
	def year(self):
		return self.__npDate.year

	@property
	def month(self):
		return self.__npDate.month

	@property
	def day(self):
		return self.__npDate.day

	@property
	def week_day(self):
		return self.__npDate.weekDay()

	@property
	def hour(self):
		return self.__npTime.hour

	@property
	def minute(self):
		return self.__npTime.minute

	@property
	def second(self):
		return self.__npTime.second


class HumanizeDateTime:
	"""
	HumanizeDate converts NepaliDateTime to nepali human readable form
	"""

	__past_text = "अघि"
	__future_text = "पछि"
	__now_text = "भर्खरै"
	__year_text = "वर्ष"
	__month_text = "महिना"
	__day_text = "दिन"
	__hour_text = "घण्टा"
	__minute_text = "मिनेट"
	__second_text = "सेकेन्ड"

	def	__init__(self, datetime_obj, *args, **kwargs):
		if type(datetime_obj) == NepaliDateTime:
			self.datetime_obj = datetime_obj.to_datetime()
		else:
			self.datetime_obj = datetime_obj
		self.threshold = kwargs.get('threshold')
		self.format = kwargs.get('format')
		self.seconds = None


	def __calc_seconds(self):
		current_date_time = datetime.datetime.now()
		current_date_time = current_date_time.replace(tzinfo=None)
		date = self.datetime_obj.replace(tzinfo=None)
		self.seconds = int((current_date_time-date).total_seconds())
		self.interval_tense = self.__past_text
		if(self.seconds < 0):
			self.interval_tense = self.__future_text

	def to_str(self):
		self.__calc_seconds()	# refreshing seconds
		seconds = self.seconds
		if( seconds < 0):
			seconds = 0 - seconds

		if not self.threshold == None:
			if( seconds >= self.threshold):
				return self.get_datetime().strip()
		
		return self.get_humanize().strip()


	def get_humanize(self):
		"""
		returns humanize datetime
		"""
		self.__calc_seconds()	# refreshing seconds

		interval_value = 0
		interval_text = ""
		if( self.seconds == 0 ):
			# now
			return self.__now_text

		elif( self.seconds < 60):
			# seconds
			interval_value = self.seconds
			interval_text = self.__second_text
			
		elif( self.seconds < 3600):
			# minute
			interval_value = self.seconds//60
			interval_text = self.__minute_text

		elif( self.seconds < 86400):
			# hour
			interval_value = self.seconds//3600
			interval_text = self.__hour_text

		elif( self.seconds < 2592000):
			# day
			interval_value = self.seconds//86400
			interval_text = self.__day_text

		elif( self.seconds < 946080000):
			# month
			interval_value = self.seconds//2592000
			interval_text = self.__month_text

		else:
			# year
			interval_value = self.seconds//946080000
			interval_text = self.__year_text

		interval_value = NepaliChar.number(interval_value)
		return str(interval_value)+' '+str(interval_text)+' '+self.interval_tense


	def get_datetime(self):
		"""
		returns date in nepali characters
		"""
		if not self.format:
			self.format = '%B %d, %Y'
		ndt = NepaliDateTime.from_datetime(self.datetime_obj)
		return ndt.strftime(self.format)

	def __str__(self):
		return self.to_str()

	def __repr__(self):
		return str(self)


class NepaliDateTimeFormater:

	format_map = {
		'a': 'weekdayHalf',
		'A': 'weekdayFull',
		'w': 'weekdayNumber',
		'd': 'day',
		'b': 'monthFull',
		'B': 'monthFull',
		'm': 'monthNumber',
		'y': 'yearHalf',
		'Y': 'yearFull',
		'H': 'hour24',
		'I': 'hour12',
		'p': 'ampm',
		'M': 'minute',
		'S': 'second'
	}

	def __init__(self, npDateTime, english=False):
		self.npDateTime = npDateTime
		self.english = english

	def __str__(self):
		return str(self.npDateTime)

	def get_str(self, format):
		i, n = 0, len(format)
		time_str = []
		try:
			while i < n:
				ch = format[i]
				i += 1
				if ch == '%':
					if i < n:
						ch = format[i]
						if ch == '%':
							time_str.append('%')
						else:
							time_str.append(getattr(self, self.format_map.get(ch)))
						i += 1
				else:
					time_str.append(ch)
		except Exception:
			raise Exception('Invalid datetime format')
		time_str = ''.join(time_str)

		return time_str

	@property
	def weekdayHalf(self):
		"""
		%a
		"""
		if self.english:
			return EnglishChar.half_day(self.npDateTime.week_day)
		return NepaliChar.half_day(self.npDateTime.week_day)

	@property
	def weekdayFull(self):
		"""
		%A
		"""
		if self.english:
			return EnglishChar.day(self.npDateTime.week_day)
		return NepaliChar.day(self.npDateTime.week_day)

	@property
	def weekdayNumber(self):
		"""
		%w
		"""
		if self.english:
			return str(self.npDateTime.week_day-1)
		return NepaliChar.number(self.npDateTime.week_day-1)

	@property
	def day(self):
		"""
		%d
		"""
		day = str(self.npDateTime.day)
		if len(day) < 2:
			day = '0'+day

		if self.english:
			return str(day)
		return NepaliChar.number(day)

	@property
	def monthFull(self):
		"""
		%B or %b
		"""
		if self.english:
			return EnglishChar.month(self.npDateTime.month)
		return NepaliChar.month(self.npDateTime.month)

	@property
	def monthNumber(self):
		"""
		%m
		"""
		month = str(self.npDateTime.month)
		if len(month) < 2:
			month = '0'+month
		if self.english:
			return str(month)
		return NepaliChar.number(month)

	@property
	def yearHalf(self):
		"""
		%y
		"""
		if self.english:
			return str(self.npDateTime.year)[2:]
		return NepaliChar.number(str(self.npDateTime.year)[2:])

	@property
	def yearFull(self):
		"""
		%Y
		"""
		if self.english:
			return str(self.npDateTime.year)
		return NepaliChar.number(self.npDateTime.year)
	
	@property
	def hour24(self):
		"""
		%H
		"""
		if self.english:
			return str(self.npDateTime.hour)
		return NepaliChar.number(self.npDateTime.hour)
	
	@property
	def hour12(self):
		"""
		%I
		"""
		hour = self.npDateTime.hour
		if hour > 12:
			hour = hour - 12
		if hour == 0:
			hour = 12
		hour = str(hour)
		if len(hour) < 2:
			hour = '0'+hour

		if self.english:
			return str(hour)
		return NepaliChar.number(hour)
	
	@property
	def ampm(self):
		"""
		%p
		"""
		if self.english:
			ampm = 'AM'
			if self.npDateTime.hour > 12:
				ampm = 'PM'
			return str(ampm)

		ampm = ''
		if self.npDateTime.hour < 12:
			ampm = 'शुभप्रभात'
		elif self.npDateTime.hour >= 12 and self.npDateTime.hour < 18:
			ampm = 'मध्यान्ह'
		else:
			ampm = 'अपरान्ह'
		return str(ampm)
	
	@property
	def minute(self):
		"""
		%M
		"""
		minute = str(self.npDateTime.minute)
		if len(minute) < 2:
			minute = '0'+minute
		if self.english:
			return str(minute)
		return NepaliChar.number(minute)
	
	@property
	def second(self):
		"""
		%S
		"""
		second = str(self.npDateTime.second)
		if len(second) < 2:
			second = '0'+second
		if self.english:
			return str(second)
		return NepaliChar.number(second)