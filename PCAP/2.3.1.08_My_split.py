# PCAP preparation
# ===================
# 📆 2022-07-05 10:44:12

def my_split(strng):
    res = []
    tmp = ''
    delimiters = [' ', ",", ]

    for l in strng:
        if l not in delimiters:
            tmp+=l
        else:
            if tmp != '':
                res.append(tmp)
                tmp = ''
    return res

print(my_split("To be or not to be, that is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))