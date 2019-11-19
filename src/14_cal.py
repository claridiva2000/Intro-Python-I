"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import date
import re


 

# print(calendar.weekheader(3))
# print()
# print(calendar.firstweekday())

# print(calendar.month(2019, 11))
 
# print(date.today())



mm_input = input("enter a month: ")
yr_input = input("enter a year: ")

if mm_input.match('\W') == True or yr_input.isalpha() == True:
    print('please only enter numbers')

elif mm_input != '' and yr_input == '':
    print(calendar.month(2019, int(mm_input)))

elif mm_input != '' and yr_input != '':
    print(calendar.month(int(yr_input), int(mm_input)))

elif mm_input == '' and yr_input == '':
    print(calendar.month(2019, 11))

# planner = Calendar(mm_input, yr_input)
# print(planner)

# print(f'{mm_input}/{yr_input}')

# mm_input + yr_input  == '':
#     empty = date.today()
#     # m=int(float(empty[0]))
#     # y=int(empty[1])
#     # print(type(m))
#     # print(type(11))
#     # print(y)
#     print(int(empty))