# PCAP preparation
# ===================
# Created: 📆 2022-07-05 10:44:12
# Changed: 📆 2023-08-08 12:39:43


def my_split(strng, dl):
    res = []
    tmp = ''

    for l in strng:
        if l not in delimiters:
            tmp+=l
        elif tmp:
            res.append(tmp)
            tmp = ''
    if tmp:
        res.append(tmp)
    return res

delimiters = [' ', ","]

print(my_split("To be or not to be, that is the question", dl=delimiters))
print(my_split("To be or not to be,that is the question", dl=delimiters))
print(my_split("   ", dl=delimiters))
print(my_split(" abc ", dl=delimiters))
print(my_split("", dl=delimiters))
