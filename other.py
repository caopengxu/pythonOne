import time
import gc

time.sleep(0.1)

a = [11, 22, 33]
b = a
# c = (a, b)
# e = c

print(id(a))
print(id(b))
# print(id(c))
# print(id(e))

if a == b:
    print("123")

if a is b:
    print("123")

c = 99999
d = 99999
print(id(c))
print(id(d))
if c is d:
    print("========")


def login(func):
    def temp():
        func()
    return temp


@login
def f1():
    print("f1")


@login
def f2():
    print("f2")


# one = login(f1)
# one()
f1()
f2()

print(gc.get_count())
print(gc.get_threshold())
gc.set_threshold(701, 11, 11)
print(gc.get_threshold())

print(gc.garbage)
gc.collect()  # 主动回收
print(gc.garbage)

