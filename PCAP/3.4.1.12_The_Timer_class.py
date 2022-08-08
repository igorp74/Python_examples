def d2(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s

class Timer:
    def __init__(self, h=0, m=0, s=0 ):
        self.__h = h
        self.__m = m
        self.__s = s

    def __str__(self):
        self.__res = f'{d2(self.__h)}:{d2(self.__m)}:{d2(self.__s)}'
        return self.__res

    def next_second(self):
        self.__s += 1
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
            if self.__m > 59:
                self.__m = 0
                self.__h += 1
                if self.__h > 23:
                    self.__h = 0

    def prev_second(self):
        self.__s -= 1
        if self.__s < 0:
            self.__s = 59
            self.__m -= 1
            if self.__m < 0:
                self.__m = 59
                self.__h -= 1
                if self.__h < 0:
                    self.__h = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
