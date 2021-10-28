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

someday = datetime(1997, 3, 19)
print(someday.weekday())
print(someday.isoweekday())