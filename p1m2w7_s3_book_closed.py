#Book closed if you can.
#Extend the W6 counter: read a file, count each word (lowercased)
#then print **the ten most common words with their counts**, in order.
#This is py4e's own capstone for Ch.10 and the first genuinely useful corpus tool you'll own.
#Sanity check: on ordinary English text the top of the list should be `the`, `and`, `of`, `to`… 
#If it isn't, something's wrong — and *knowing what the answer should look like before you run it* is itself a research skill.
fhand = open('mbox-short.txt')
counts=dict()
lst = list()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
for key, val in counts.items():
    lst.append((val, key))
lst.sort(reverse=True)
for (val, key) in lst[:10]:
    print(val, key)