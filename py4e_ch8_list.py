fname = input('Enter file name:')
fh = open(fname)
for line in fh:
    lst = line.rstrip()
    split_lst = lst.split()
    print(split_lst)
