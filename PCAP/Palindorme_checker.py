# PCAP preparation
# ===================
# 📆 2022-07-05 10:40:57

str_in = 'Ten animals I slam in a net'

clean_str  = str_in.lower().replace(' ','')
revert_str = clean_str[::-1]

print('Original: ',clean_str)
print('Reverted: ',revert_str)

if clean_str == revert_str:
    print('✔ It is a palindorme')
else:
    print('❌ Not a palindorme')
