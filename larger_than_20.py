fname = input('Enter file name:')
fh = open(fname)
for line in fh:
    line = line.rstrip()
    words = len(line)
    if words > 20:
        print(line)
    else:
        continue

