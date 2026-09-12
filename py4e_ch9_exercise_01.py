#9.4 Write a program to read through the mbox-short.txt 
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#  The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
base = dict()
handle = open('mbox-short.txt')
new_list = list()
for line in handle:
    if line.strip() == '' or not line.startswith('From '): continue
    line = line.rstrip()
    new_line = line.split()
    new_list.append(new_line[1])
for word in new_list:
    word.lower()
    base[word] = base.get(word, 0) + 1
#print(base)
namecount = None
numcount = None
for name, num in base.items():
    if numcount is None or num > numcount:
        numcount = num
        namecount = name
        print(namecount, numcount)
