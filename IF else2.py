import sys

N = int(input(3).strip())

if N % 2 != 0:
    print("Weird")
else:
    if 2 <= N <= 5:
        print("Not Weird")
    elif 6 <= N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
