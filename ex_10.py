fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)

many = dict()
for line in fhand:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w,0)+1


# Find the top 5 words by frequency

tmp = dict()
newlist = list()
for k,v in many.items() :
    tup = (v,k)
    newlist.append(tup)
    print(tup)

cool = sorted(newlist, reverse=True)
print(cool)

for v,k in cool[:5] :
    print(k,v)