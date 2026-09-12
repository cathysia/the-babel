fname = input('Enter file name:')
fh = open(fname)
count = 0
count_number = 0
for line in fh:
 if not line.startswith('X-DSPAM-Confidence:') : 
    continue
 line = line.strip()
 number = line.find('0')
 extract = line[number:]
 count = count + float(extract)
 count_number = count_number + 1
print('Average spam confidence:',float(count) / float(count_number))