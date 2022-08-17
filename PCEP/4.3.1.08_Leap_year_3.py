def is_year_leap(year):
    result = False

    if (year % 400 == 0) and (year % 100 == 0):
        result = True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        result = True

    return result

def days_in_month(year, month):
    if month not in range(1,13): return
    dim = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        dim[1]=29
    return dim[month-1]

def day_of_year(year, month, day):
    if month not in range(1,13): return
    res = 0
    dim = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        dim[1]=29

    if day > dim[month-1]:return

    if month>1:
        for i in dim[:month-1]:
            res += i
    return (day+res)

print(day_of_year(2000, 3, 31))
