def is_pass(score):
    return score>=60
def report(score):
    if is_pass(score):
        return 'pass'
    else:
        return 'fail'
def f(yeoo):
    return 'yeoo'
print(report(75))
print(report(42))
print(f(yeoo))