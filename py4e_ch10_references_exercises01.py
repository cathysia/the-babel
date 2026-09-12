#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

fhand = open('mbox-short.txt')
sender = dict()
import string
lst = list()

for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    address = words[1]
    sender[address] = sender.get(address,0)+1
tup = list(sender.items())
for v, k in tup:
    lst.append((k, v))
lst.sort(reverse=True)
print(lst)