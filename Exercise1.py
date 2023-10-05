


def return_distinct(num1, num2, num3):
    n_sum = num1 + num2 + num3
    list = [num1, num2, num3]

    if n_sum < 10:
        return min(list)
    elif n_sum > 15:
        return max(list)
    else:
        list.sort()
        return list[1]


print(return_distinct(5, 5, 5))
