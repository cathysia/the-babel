#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fhand = open('mbox-short.txt')
lst = dict()
import string
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.split()
    time = line[5]
    hour = time[:2]
    lst[hour] = lst.get(hour,0)+1
tup = list(lst.items())
tup.sort()
for key, val in tup:
    print(key, val)