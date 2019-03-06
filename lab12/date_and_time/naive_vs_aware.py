import datetime,pytz

unaware = datetime.datetime(2018, 11, 21, 9, 12, 32, 0)
aware_by_pytz = datetime.datetime(2018, 11, 21, 9, 12, 32, 0, pytz.UTC)

print(unaware)
print(aware_by_pytz)
print(unaware == aware_by_pytz)


# returns naive datetime object
today = datetime.datetime.today()

# equivalent to datetime.today(), when no tzinfo object is passed
now = datetime.datetime.now()

# returns the UTC time
utcnow = datetime.datetime.utcnow()

print(today)
print(now)
print(utcnow)

