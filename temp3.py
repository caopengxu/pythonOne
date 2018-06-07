numbers = [i for i in range(1, 6) if i % 2 == 0]
print(numbers)

strings = [["1", "2", "3"], ["3", "4", "5"], ["6", "7", "8"]]
flatten = [int(i) for item in strings for i in item]
print(flatten)

xx = [2, 3, 5]
yy = [2, 3, 4]

points = [(x, y) for x in xx for y in yy if x != y]
print(points)

numbers1 = {i for i in range(1, 6) if i % 2 == 0}
print(numbers1)

numbers2 = {i: str(i) for i in range(1, 6) if i % 2 == 0}
print(numbers2)
switch = {value: key for key, value in numbers2.items()}
print(switch)

# ------------------------------------------------------
# AttributeError
# "hello".size

# IndexError
# (1, 2)[2]

# KeyError
# {"a": 1}["b"]

# NameError
# temp()

# SyntaxError
# temp(

# TypeError
# "hello".index(1)

# ValueError
# int("s")

# ZeroDivisionError
# 3/0

try:
    3 / 0
    # 3/1
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("NameError")
# except:
#     print("error")
else:
    print("No errors.")
finally:
    print("Clean up actions")
