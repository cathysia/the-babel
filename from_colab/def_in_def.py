def is_pass(score):
    return score>=60
def report(score):
    if is_pass(score):
        return 'pass'
    else:
        return 'fail'
score = input('enter your score')
score = int(score)
print(report(score))