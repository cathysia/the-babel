#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
#Your program should convert all the input to lower case and only count the letters a-z. 
#Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
#Find text samples from several different languages and see how letter frequency varies between languages.
#Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
fhand = open('romeo-full.txt')
import string
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if 'a' <= letter <= 'z':
                if letter not in counts:
                    counts[letter] = 1
                else:
                    counts[letter] += 1
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)
print(lst)