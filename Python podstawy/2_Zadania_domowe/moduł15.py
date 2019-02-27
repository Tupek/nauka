import random

def random_average(n):
    sum = 0
    i = 0
    while i < n:
        x = random.randint(0, 100)
        sum = sum + x
        i = i + 1
    return sum / n

print(random_average(5))