# Day 16 of python Exercise
#Question (1)
#Get the current day, month, year, hour, minute and timestamp from datetime module
# importing the required functions
from datetime import datetime   # get current datetime object
now = datetime.now()
# extract day, month, year, hour, minute
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
# create timestamp using strftime method
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
# print the values
print("Day:", day)
print("Month:", month)
print("Year:", year)
print("Hour:", hour)
print("Minute:", minute)
print("Timestamp:", timestamp)

#Question (2)
#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
from datetime import datetime

# get current datetime object
now = datetime.now()

# format the date using strftime method
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

# print the formatted date
print("Formatted date:", formatted_date)

#Question (3)
#Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
print(f'Date_string =', {date_string})
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

#Question (4)
#Calculate the time difference between now and new year.
from datetime import datetime
# get current time and New Year's Day time
current = datetime.now()
new_year = datetime(current.year + 1, 1, 1)

# calculate time difference
time_difference = new_year - current

# print the time difference in days, hours, and minutes
days = time_difference.days
hours = time_difference.seconds // 3600
minutes = (time_difference.seconds // 60) % 60
print("Time until New Year's Day: {} days, {} hours, {} minutes".format(days, hours, minutes))

#Question (5)
#Calculate the time difference between 1 January 1970 and now.
from datetime import datetime

# get Unix epoch time and current time
posix = datetime.utcfromtimestamp(0)
current = datetime.now()

# calculate time difference
time_difference = now - posix

# print the time difference in days, hours, minutes, and seconds
days = time_difference.days
hours = time_difference.seconds // 3600
minutes = (time_difference.seconds // 60) % 60
seconds = time_difference.seconds % 60
print("Time since Unix posix: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))


#The time difference between now and 1 January, 1970,midnight in seconds is 1676922856.741553
#The time difference in days: 19408 days, 0:00:00

#Question (6)
'''Think, what can you use the datetime module for? Examples:
Time series analysis
To get a timestamp of any activities in an application
Adding posts on a blog'''


