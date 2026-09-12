#Session 4 — Real text [frag] · Run your Top Ten on something substantial. 
# Download a public-domain book as plain text (Project Gutenberg, gutenberg.org — pick anything you'd enjoy) and run it. 
# Then notice two things: how long the tail of rare words is, and how the punctuation problem from W4 shows up again ("the," vs "the"). 
# Don't fix it — just observe it. 
#That observation is Zipf's law and tokenization, both arriving early and on their own.
import string
fhand = open('Count_of_Mont_Cristo.txt')
counts = dict()
lst = list()
for line in fhand:
    #line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.split()
    for words in line:
        words = words.lower()
        counts[words] = counts.get(words,0)+1
for key, val in counts.items():
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:10]:
    print(key, val)