# import this
import math as m
# from math import *
from math import gcd

print(m.gcd(4, 6))
print(gcd(4, 6))


# ------------------------------
def temp_px():
    pass


def add(a, b):
    return a + b


def add_one(*args):
    temp = 0
    for i in args:
        temp += i
    return temp


def add_two(**kargs):
    temp = 0
    for i in kargs:
        temp += kargs[i]
    return temp


def add_other(*args, **kargs):
    temp = 0
    for i in args:
        temp += i

    for i in kargs:
        temp += kargs[i]
    return temp


print(add(1, 2))
print(add(3, 5))
print(add_one(1, 3, 5, 6))
print(add_two(n1=1, n2=2, n3=3))
print(add_other(1, 2, n1=3, n2=4))
