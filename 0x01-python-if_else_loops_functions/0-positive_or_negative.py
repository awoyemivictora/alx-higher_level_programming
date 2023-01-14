#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if (number > 0):
    print(number)
    print("is positive")
elif (number == 0):
    print(number)
    print("is zero")
else:
    print(number)
    print("is negative")
