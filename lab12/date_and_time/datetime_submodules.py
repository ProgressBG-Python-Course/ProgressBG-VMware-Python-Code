import datetime as dt

lunch_time = dt.time(hour=12, minute=0, second=0)
print(f"lunch_time: {lunch_time}")

due_date = dt.date(2019, 3, 7)
print(f"due_date: {due_date}")

now = dt.datetime.now()
print(f"now: {now}")


due_date = dt.date(2019, 3, 7)
current_date = dt.datetime.now().date()

print(due_date - current_date)