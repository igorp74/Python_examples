# PCAP preparation
# ===================
# 📆 2022-06-30 10:46:01



# Let's define a few test words'
s1 = 'Listen'
s2 = 'Silent'

# Fastest way - using sorted function and lower() method
#-------------------------------------------------------------
if sorted(s1.lower()) == sorted(s2.lower()):
    print('Anagram')
else:
    print('It is not an anagram')


# Alternative way - using dictionary for counting the letters frequency in string
# This way I don't need to use sorted() function
#-------------------------------------------------------------

def count_dict(str):
    dc = {}
    for l in str.lower():
        if l not in dc:
            dc[l] = 1
        else:
            dc[l] += 1
    return dc

d1 = count_dict(s1)
d2 = count_dict(s2)

if d1 == d2:
    print('Anagram')
else:
    print('Jokjuar Haljimi')
