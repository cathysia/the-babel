fh = open('mbox-short.txt')
count = 0
for line in fh:
    line = line.rstrip()
    line = line.split()
    #print(line)
    for word in line:
        if not word.startswith('From'): continue
        if word.startswith('From:'): continue
        print(line[1])
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')