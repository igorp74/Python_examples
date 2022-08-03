# PCAP preparation
# ===================
# 📆 2022-06-30 10:46:01


# Let's define a few test words'
s1   = 'dog'
s2_o = 'vcxzxduybfdsobywuefgas'
s2   = s2_o
# Need accumulator for storing the matching letters
acc = []

# Idea is to loop over first string
# and inside that loop through string two
# Also, I would enumerate first string so I can check positions

for e,c in enumerate(s1.lower()):
    for l in s2.lower():
        # If there is a match
        if l == c:
            # Make second string shorter
            # by slicing it on the current position till the end
            s2 = s2[s2.index(l):]

            # Check if something is in accumulator
            if len(acc):
                # if yes, check the appropriate position
                if len(acc) == e:
                    # if position is ok, add letter
                    acc.append(l)

            # if accumulator is empty, just add the first match
            else:
                acc.append(l)

print('I am looking for this word: ', s1)
print('          inside this word: ', s2_o)

# Finally, join the accumulator into the string
res = ''.join(acc)
# and match with the original first string
if s1==res:
    print('\n✔✔✔ and I found it! ✔✔✔\n')
else:
    print('\n❌❌❌ but I did not find it! ❌❌❌\n')


