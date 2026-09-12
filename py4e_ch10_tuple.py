#z = (5, 4, 3)
#z[3] = 2
#(x, y) = (4, 'fred')
#print(y)
#d = dict()
#d['csev'] = 2
#d['cwen'] = 4
#for (k, v) in d.items():
#    print(k, v)
#tups = d.items()
#print(tups)
d = {'a': 10, 'c':22, 'b':1}
#dict_items = d.items()
#print(dict_items) #[('a',10), ('c',22), ('b',1)]))
#print(sorted(d.items()))
#for k, v in sorted(d.items()):
#    print(k,v)
#tmp = list()
#for k,v in d.items():
#    tmp.append((v,k))
#print(tmp)
#tmp = sorted(tmp)#, reverse=True)
#print(tmp)

#counts=dict()
#for line in open('mbox-short.txt'):
#    words = line.split()
#    for word in words:
#        counts[word] = counts.get(word,0) + 1
#lst = list()
#for key, val in counts.items():
#    newtup = (val, key)
#    lst.append(newtup)

#lst = sorted(lst, reverse=True)
#for val, key in lst[:10]:
#    print(key, val)

#c = {'a':10, 'b':1, 'c':22}
#print(sorted([(v,k) for k,v in c.items()]))