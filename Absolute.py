def absolute_sum(*args):
    sum = 0
    for i in args:
        sum += abs(i)
    return sum

print(absolute_sum(1,-3,4,-6))