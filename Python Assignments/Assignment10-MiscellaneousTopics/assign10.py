from datetime import datetime, timedelta

# a) Current date and time
current_datetime = datetime.now()
print(f"a) Current Date and Time: {current_datetime}")

# b) Current year
current_year = current_datetime.year
print(f"b) Current Year: {current_year}")

# c) Month of year
month_of_year = current_datetime.strftime("%B")
print(f"c) Month of Year: {month_of_year}")

# d) Week number of the year
week_number = current_datetime.strftime("%U")
print(f"d) Week Number of the Year: {week_number}")

# e) Weekday of the week
weekday = current_datetime.strftime("%A")
print(f"e) Weekday of the Week: {weekday}")

# f) Day of year
day_of_year = current_datetime.strftime("%j")
print(f"f) Day of Year: {day_of_year}")

# g) Day of the month
day_of_month = current_datetime.strftime("%d")
print(f"g) Day of the Month: {day_of_month}")

# h) Day of week
day_of_week = current_datetime.strftime("%w")
print(f"h) Day of Week (0-6, where 0 is Sunday): {day_of_week}")

# Determine whether a given year is a leap year
year = int(input("Enter a year to check if it's a leap year: "))
leap_year = "Leap" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not Leap"
print(f"{year} is a {leap_year} Year")

# Get the current time
current_time = datetime.now().strftime("%H:%M:%S.%f")
print(f"Current Time: {current_time}")

# Subtract five days from the current date
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print(f"Sample Date: {current_date.strftime('%Y-%m-%d')}")
print(f"5 days before Current Date: {five_days_ago.strftime('%Y-%m-%d')}")
