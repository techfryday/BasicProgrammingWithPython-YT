from datetime import datetime
import pytz
dt = datetime.now()
""" print(dt.day)
print(dt.month)
print(dt.year)
print(dt.weekday()) # Monday as 0 and further
print(dt.isoweekday()) # Monday as 1 and further """


""" # tzinfo is None hence dt is a naive object
print(dt.tzinfo) """

tz = pytz.timezone("Asia/Kolkata")
awaredt = tz.localize(dt)
# print(awaredt.tzinfo)

dt1 = datetime(1985, 5, 13, 0, 0 ,0 ,0)
dt2 = datetime(1999, 11, 16, 0, 0 ,0 ,0)
diff = dt2 - dt1
print(dt1)
print(dt2)
print(diff)