c0 = 1023

cnt = 0

while c0 != 1:
    cnt += 1

    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3*c0 + 1
    print(c0)
print('steps =',cnt)