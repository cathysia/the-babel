#write a function scale(v, k) that takes a list [x, y] and a number
#returns the scaled list — the code version of what the video shows
def scale(v, k):
    return [v[0] * k, v[1] * k]
print(scale([2, 3], 2))