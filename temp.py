aNumber = 123
aString = str(aNumber)

action = "Hello"
name = "Mars!"

print(dir(action))
# print(help(action.count))

print("%s %s" % (action, name))
print("Hello %s" % name)
print("PI: %.2f" % 3.14)

welcome = {"action": "Hello", "name": "Mars"}
print("%(action)s %(name)s" % welcome)

print("{0} {1}".format(action, name))
print("{action} {name}".format(**welcome))

# ----------------------------------------
list1 = []
list2 = list()
print(dir(list2))

numlist = [8, 3, 5]
mixList = [1, "one", 1.0]

addList = [numlist, mixList]

print(numlist + mixList)
print(mixList.extend(numlist))
print(mixList)

numlist.append(9)
# numlist.append([3, 2])

numlist1 = numlist.copy()
numlist.sort()
print(numlist)
print(numlist1)

print(numlist[0])
print(numlist[0:3])
print(numlist[0:-1])
numlist = [1, 2, 3, 4]
print(numlist)
print(numlist[::-1])

numlist.insert(0, 2)
print(numlist)

# print(numlist.pop(0))
# print(numlist.remove(3))
# print(numlist)

# del(numlist[0])
# del(numlist[0:5])
del numlist[:5:2]
# del(numlist[0:5:2])
print(numlist)

print(numlist.index(3))

print(len(numlist))
