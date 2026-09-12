#fruit = 'banana'
#for letter in fruit:
#    print(letter)

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

word = 'duri'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

if word == 'banana':
    print('alright, banana.')

if word > 'banana':
    print('your word' + word + 'comes before banana')
#word > 'banana' compares strings lexicographically (character by character, by Unicode code point). With word = 'duri', comparing first characters: 'd' > 'b' is True (100 > 98), so the whole expression is True — the if block runs.

#Worth noting: the message on fruit_banana.py:23 says "comes before banana", but that's backwards — if word > 'banana' is true, word actually comes after 'banana' alphabetically. That looks like a bug in the print text.