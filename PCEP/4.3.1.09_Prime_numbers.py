def is_prime(num):
    flag = False # not prime number
    if num == 1:
        flag = True
    else:
        cn = 0
        for i in range(2,num+1):
            if num%i == 0:
                cn += 1
        if cn <= 1:
            flag = True
    return flag

for i in range(1, 90):
	if is_prime(i):
			print(i, end=" ")
print()
