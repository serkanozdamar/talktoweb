from datetime import datetime, UTC

x = datetime.now()
print(type(x))
print(x)
print(x.utcoffset())
print(x.now(UTC))

print(x.year)
print(x.month)
print(x.day)
print(x.date())

print(x.strftime("%A"))

from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)
print(date_time)