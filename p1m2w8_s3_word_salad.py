import random
import re

fhand = open('Count_of_Mont_Cristo.txt')
text = fhand.read()
text = text.lower()
start = text.rfind('chapter 1.')
end = text.rfind('footnotes:')
if start == -1 or end == -1:
    print('Marker not found', start, end)
    quit()
else:
    words = re.findall(r'\w+', text[start:end])
#    print(words[:20])
#    print(words[-20:])

salad = ''
for i in range(50):
    word = random.choice(words)
    salad = salad + ' ' + word
print(salad)