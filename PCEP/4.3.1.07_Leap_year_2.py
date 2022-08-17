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
    dim = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        dim[1]=29
    return dim[month-1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
