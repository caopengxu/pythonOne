def temp():
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a + b


a = temp()
# for i in a:
#     print(i)
print(next(a))
print(a.__next__())
print(next(a))
print(a.__next__())
print(a.__next__())


def temp1():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


b = temp1()
# print(b.__next__())
print(b.__next__())
print(b.send("heihei "))
print(b.send("haha"))
print(b.__next__())
# for i in b:
#     print(i)
