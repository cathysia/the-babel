text = 'X-DSPAM-Confidence:   0.8475'
find_space_first = (text.find(' '))
print(find_space_first)
count = 0
for space in text:
    if space == ' ':
        count = count + 1
print(count)

position = int(find_space_first) + int(count)
print(position)

print(text[position:])

text = 'hellow word'
print(len(text))