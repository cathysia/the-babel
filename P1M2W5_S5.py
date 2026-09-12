#read a text file, build a list of all words
#print (a) the number of words, (b) the first ten, (c) the longest one. All tools already yours.
fh = open('mbox-short.txt')
lst = list()
count = 0
longest = None
for line in fh:
    line = line.rstrip()
    #print(line)
    lst.append(line)
print(len(lst))
print(lst[0:10])
for words in lst:
    if longest is None or words > longest:
        longest = words
print(longest)