def sum_squares(*args):


    sum_of_squares = 0
    for arg in args:
        sum_of_squares += arg ** 2
    return sum_of_squares


# Example usage:

print(sum_squares(1, 2, 3))
print(sum_squares(10, 20, 30))
