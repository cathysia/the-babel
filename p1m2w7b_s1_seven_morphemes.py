import re
hand = open('mbox-short.txt')

for line in hand:
    line= line.rstrip()
#    stuff = re.findall('[0-9]+', line)
#    print(stuff)
#    stufff = re.findall('[0-9]*', line)
#    print(stufff)
    stuff = re.findall(':\d', line) #switch the pattern to try different outcome
    if len(stuff) == 0: continue
    print(line)