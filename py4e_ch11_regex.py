#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    if line.startswith('From:'):
#        print(line)
#    if line.find('From:') >= 0:
#        print(line)

#import re
#for line in hand:
#    line = line.rstrip()
#    if re.search('From:', line):
#    if re.search('^From:', line):
#        print(line)
import re
#hand = open('romeo-full.txt')
#for line in hand:
#    line = line.rstrip()
#    if re.search('^T.*', line):
#        print(line)
#x = 'My 2 favorite numbers are 19 and 42'
#y = re.findall('[aeiou]+', x)
#print(y)

fhand = open('mbox-short.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
#    if re.findall('@([^ ]*?)', line):
#        y = re.findall('@([^ ]*)',line)
#        print(y)

#    if re.findall('^T.+:', line):
#        print(line)
#    if re.search('^T.+:', line):
#        print(line)
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)