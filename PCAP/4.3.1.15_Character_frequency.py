# Read the text file
#-----------------------------------------------------
with open('samplefile.txt') as f:
    lines = f.readlines()

# Prepare analytics - in this case dictionary who will collect
# letters and count frequencies
#-----------------------------------------------------
acc = {}
for l in lines:
    l = l.replace('\n','')
    for c in l:
        if c not in acc:
            acc[c.lower()] = 1
        else:
            acc[c.lower()] += 1

# Sort result dictionary ...
#-----------------------------------------------------
res = dict(sorted(acc.items(), key=lambda x:x[1], reverse = True))

# ...and present the result
for k,v in res.items():
    print(k,v)
