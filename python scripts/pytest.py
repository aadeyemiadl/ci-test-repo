"""
This module contains utility functions for handling user authentication.
"""
# pylint: disable=consider-using-f-string

# Python program to check if year is a leap year or not

YEAR = 2000
# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (YEAR % 400 == 0) and (YEAR % 100 == 0):
        print("{0} is a leap year".format(YEAR))
i ajd ekl
dfa
str(lkfs) = 2 

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (YEAR % 4 ==0) and (YEAR % 100 != 0):
        print("{0} is a leap year".format(YEAR))
#
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
 else:
        print("{0} is not a leap year".format(YEAR))
