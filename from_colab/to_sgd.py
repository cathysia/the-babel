def to_sgd(x):
    return(x*1.35)
print(to_sgd(100))

def is_senior(x):
    return x>8
def evaluate(x):
    if is_senior(x):
        print('senior')
    else:
        print('junior')
first_x = input('ur yeas of experience')
intx = int(first_x)
x = intx
evaluate(x)