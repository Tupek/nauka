import random

def d6(num):
    sum = 0
    for i in range(0,num):
        roll = random.randint(1, 6)
        sum = sum + roll
        print(roll)
    return sum

moj = d6(7)
print(moj)

