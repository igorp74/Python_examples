def is_year_leap(year):
    result = False
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        result = True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        result = True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        pass

    return result

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("✔")
	else:
		print("❌")