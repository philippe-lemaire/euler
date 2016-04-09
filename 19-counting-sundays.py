'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import calendar

# usage : calendar.monthrange(2016,5) returns the index of the first day of May 2016, and the number of days of this month

sundays_first = 0

for year in range (1901, 2001):
    for month in range (1, 13):
        if 6 in calendar.monthrange(year, month):
            sundays_first += 1

print("Number of Sundays that fell on the first of the month during the twentieth century = ", sundays_first)
