import datetime

current_date = datetime.date.today()

# TASK 1: print the current date with format: day.month.full_year
# 6.3.2019

# print( current_date.strftime('%d.%m.%Y') )


# TASK 2: create a date object for the '2018.03.24' and print it as 03.24.2018
date1 = datetime.datetime.strptime('2018.03.24', "%Y.%m.%d")
# print(date1.strftime('%d.%m.%Y'))



# TASK3: how many time we have from "now" until 12.00
now = datetime.datetime.now();
lunch = datetime.datetime.strptime("12.00", "%H.%M")


timediff = lunch - now

print(timediff)




