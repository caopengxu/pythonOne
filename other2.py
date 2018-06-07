class temp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        if item == "name":
            print("name")
            return "heihei"
        else:
            return object.__getattribute__(self, item)
            # return 14
            # return self.show

    @staticmethod
    def show():
        print("show")


one = temp("lala", 12)
print(one.name)
print(one.age)

one.show()

# ---------------------
two = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(type(two))
print(list(two))

three = filter(lambda x: x % 2, [1, 2, 5, 6])
print(type(three))
print(list(three))

four = sorted([1, 5, 6, 4])
print(four)

# -----------------------
a = "abcdef"
b = set(a)
print(b)

A = "bdfg"
B = set(A)

print(b & B)
print(b | B)
print(b - B)
print(b ^ B)

# -----------------------
import functools

print(dir(functools))


def action(*args, **kwargs):
    print(args)
    print(kwargs)


temp1 = functools.partial(action, 1, 2, 3)
temp1()
temp1(4, 5, 6)
temp1(a="A", b="B")

# ---------------------------
import hashlib

m = hashlib.sha256()
print(m)
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
print(m.digest())


