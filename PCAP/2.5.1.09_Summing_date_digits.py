enter_date = '12061974'

def date_counter(ds):
    res = 0
    for i in ds:
        res += int(i)
    if len(str(res))>1:
        res = date_counter(str(res))

    return res

print(date_counter(enter_date))
