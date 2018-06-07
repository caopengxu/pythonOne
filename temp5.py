class Person:
    """一个类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def wakeup(self, at):
        print("{0}--{1}".format(self.name, at))

    def __del__(self):
        print("没了")
        # super.__delattr__()


# one = Person("px", 30)
# print(one.name)
# print(one.age)
#
# print(hasattr(one, "name"))
# print(getattr(one, "name"))
#
# setattr(one, "name", "xx")
# # delattr(one, "name")
# print(one.name)
#
# one.wakeup("0:00")
# Person.wakeup(one, "0:00")
#
# twoPerson = one
# print(id(one))
# print(id(twoPerson))
#
# del one
# print("还有引用吗")
# del twoPerson
