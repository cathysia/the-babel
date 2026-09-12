fname = input('enter file name:')
fh = open(fname)
#for line in fh:
 #   if not line.startswith('X-DSPAM-Confidence:'):
  #      continue
   # line = line.strip()
    #print(line)
    #start = line.find('0.')
#    print(line[start:])

for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    line = line.rstrip()
    #print(line)
    num = line.find('0.')
    print(num)
    extract = line[num:]
    print(extract)