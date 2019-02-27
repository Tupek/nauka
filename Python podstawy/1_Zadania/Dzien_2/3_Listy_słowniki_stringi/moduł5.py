def mean(numbers):
    s = sum(numbers)
    l = len(numbers)
    m = s / l
    return m

a = [5, 5, 5.5]
m = mean(a)
print(m)
