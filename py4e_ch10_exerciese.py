#Find the 5 top word by frequency
fname = input('Enter file:')
if len(fname)<1:fname = 'clown.txt'

fhand = open(fname)
many = dict()

for line in fhand:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w, 0) + 1
print(many.items())
print(sorted(many.items(), reverse=True))

tmp = dict()
newlist = list()
for k,v in many.items():
    tup = (v,k)
    newlist.append(tup)
print(newlist)
print(sorted(newlist))
cool = sorted(newlist, reverse=True)
for v,k in cool[:5]:
    print(k,v)