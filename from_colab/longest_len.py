loooooongest = None
type(loooooongest)
words = ['syntax', 'morphology', 'tone']
for single_word in words:
    if loooooongest is None or len(single_word) > len(loooooongest):
        loooooongest = single_word
print(loooooongest)

def is_long_word(w):
    return len(w)>6
def count_long_words(text):
    count = 0
    for words in text.split():
        if is_long_word(words):
            count = count + 1
    return count
print(count_long_words('computational linguistics is so funnyyyy'))
