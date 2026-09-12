def meets_minimum_salary(offer):
    return offer>=30000
def evaluate_offer(offer):
    if meets_minimum_salary(offer):
        return('ok')
    else:
        return('nah')
print(evaluate_offer(9))