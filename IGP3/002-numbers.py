# Numbers
# =======
# Every year that is exactly divisible by four is a leap year, except for years
# that are exactly divisible by 100, but these centurial years are leap years
# if they are exactly divisible by 400.

# For example, the years 1700, 1800 and 1900 are not leap years, but the years
# 1600 and 2000 are.

# Write Python code to determine if 1800, 1900, 1903, 2000, and 2002 are leap
# years

years = [1800, 1900, 1903, 2000, 2002, 2024]

def is_leap(year):
    for year in years:
        if (year % 4 == 0) and (year % 100 != 0):
            print(f"{year} is a leap year")
        elif (year % 400 == 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")


is_leap(years)


