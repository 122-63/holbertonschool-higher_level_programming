#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
m = "Last digit of"
n = "and is less than 6 and not 0"
if number < 0:
    num = number % -10
elif number >= 0:
    num = number % 10
if num > 5:
    print("{} {:d} is {:d} and is greater than 5".format(m, number, num))
elif num == 0:
    print("{} {:d} is {:d} and is 0".format(m, number, num))
elif num < 6 and num != 0:
    print("{} {:d} is {:d} {}".format(m, number, num, n))
