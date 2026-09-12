fhand = open('Count_of_Mont_Cristo.txt')
counts=dict()
lst = list()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
for key, val in counts.items():
    lst.append((val/sum(counts.values()), key))
lst.sort(reverse=True)
top1 = lst[:10]
#print(sum(counts.values()))

fhand1 = open('Astronomy_for_Amateurs.txt')
counts1=dict()
lst1 = list()
for line1 in fhand1:
    line1 = line1.lower()
    words1 = line1.split()
    for word1 in words1:
        counts1[word1] = counts1.get(word1,0)+1
for key1, val1 in counts1.items():
    lst1.append((val1/sum(counts1.values()), key1))
lst1.sort(reverse=True)
top2 = lst1[:10]
#print(sum(counts1.values()))

matrix = tuple(zip(top1, top2))
for pair in matrix:
    print(pair)