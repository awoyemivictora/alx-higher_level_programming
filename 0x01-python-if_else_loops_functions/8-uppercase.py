#!/usr/bin/python3

z =""


def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            x = ord(i) - 32
            y = chr(x)
            z = z - y

print("best".format(z))
print("Best School 98 Battery street".format(z))

