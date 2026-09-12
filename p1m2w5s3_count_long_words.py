def words(x):
    longest = None
    for word in x.split():
        if longest is None or len(word) > len(longest):
            longest = word
    return longest
print(words('computational linguistics is surprisingly enjoyable'))