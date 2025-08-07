# # first i will do the app that gives you day based on date.

# import datetime

# day=int(input("enter a day:  "))
# month=int(input("enter a month:  "))
# year=int(input("enter a year:  "))

    
# date = datetime.date(year,month,day)
# day_number = date.weekday()
# days_names = ["monday","tuesday", "wendesday","thursday", "friday", "saterday","sunday",]
 
# print(days_names[day_number])


# def datetime(year, month, day):
#     if year == 4:
#         return year
#         if month == 
#     else: 
#         print("wrong year")

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_day_name(day_number):
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_number]

def calculate_day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

    return get_day_name(h)

# Get user input
year = int(input("Enter year (e.g., 2025): "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day (1-31): "))

# Optional leap year info
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Calculate and print the day of the week
day_name = calculate_day_of_week(year, month, day)
print(f"The day of the week is: {day_name}")