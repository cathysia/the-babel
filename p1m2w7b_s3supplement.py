fhand = open('Count_of_Mont_Cristo.txt')
counts=dict()
lst = list()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
total = sum(counts.values())
for key, val in counts.items():
    lst.append((val, key))
    if 'you' in key:
        print(key, val)
lst.sort(reverse=True)
top = lst[:10]
for single_word in top:
    print(single_word)
print(total)

import re
fhand = open('Count_of_Mont_Cristo.txt')
counts = dict()
lst = list()
for line in fhand:
    line = line.lower()
    line = line.rstrip()
    words = re.findall(r'\w+', line)
    for word in words:
        counts[word] = counts.get(word,0)+1
total = sum(counts.values())
for key, val in counts.items():
    lst.append((val, key))
    if 'you' in key:
        print(key, val)
lst.sort(reverse=True)
top = lst[:10]
for single_word in top:
    print(single_word)
print(total)