def is_long_word(w):
    return len(w)>6
def count_long_words(text):
    count = 0
    for word in text.split():
        if is_long_word(word):
            count = count + 1
    return count
print(count_long_words('mmm mmm mmmm helohelohelo computational lingistics is surprisingly enjoyable'))

def count_words(text):
    count = 0
    for words in text.split():
        count = count + 1
    return count
print(count_words('computational linsuitstics is surprisingly enjoyable!'))

print('a b c'.split())

