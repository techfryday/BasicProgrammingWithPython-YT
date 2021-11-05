from datetime import datetime
import pytz
# Aware and Naive objects
# Aware: tzinfo is available
# Naive: tzinfo is not available

""" dt = datetime.now()
print(dt)
print(dt.tzinfo) # None i.e. Naive object

tz = pytz.timezone('Asia/Kolkata')
awaredt = tz.localize(dt)
print(awaredt)
# print(awaredt.tzinfo) # Asia/Kolkata i.e. Aware object
print("--------------------------")
print(awaredt.day)
print(awaredt.month)
print(awaredt.year)
print(awaredt.hour)
print(awaredt.minute)
print(awaredt.second)
print(awaredt.microsecond)
print("%.0f"%awaredt.timestamp())
print(awaredt.time()) """

# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
# someday = datetime(1997, 3, 19)
# print(someday.weekday())
# print(someday.isoweekday())

day1 = datetime(2021, 11, 5, 14, 0, 0, 0)
day2 = datetime(2021, 11, 5, 16, 30, 0, 0)
diff = day2 - day1
print(diff)