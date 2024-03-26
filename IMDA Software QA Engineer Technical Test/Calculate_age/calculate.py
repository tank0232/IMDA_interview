# -*- coding: utf-8 -*-
import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

validation = False

while(validation == False):

    name = input("input your name: ")
    if(name.isalpha() == False):
        print('Please enter alphabet characters for Name')
        continue

    dayInput = input('input date of birth: ')
    if(dayInput.isnumeric() == False):
        print('Please enter a non-decimal digit for Day')
        continue
    if(int(dayInput) > 32):
        print('Please enter a day lesser than 32')
        continue

    monthInput = input('input month of birth: ')
    if(monthInput.isnumeric() == False):
        print('Please enter a non-decimal digit for Month')
        continue
    if(int(monthInput) > 13):
        print('Please enter a month lesser than 12')
        continue   

    age = input("input your age: ")
    if(age.isnumeric() == False):
        print('Please enter a non-decimal digit for Age')
        continue
    
    validation = True

localtime = time.localtime(time.time())
year = int(age) - 1
month = year * 12 + int(monthInput)
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))