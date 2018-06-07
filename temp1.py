empty = ()

numbers = (1, 2, 3)
mix = tuple(["a", "b", 3])
print(mix)
print(mix + numbers)
print(mix * 2)

print(numbers[0])
print(numbers[0:2])
print(numbers[0:3:2])

print(len(numbers))
print(min(numbers))
print(max(numbers))

print(2 in numbers)

del numbers
# print(numbers)

# -------------------------------
dic = {}
user = {"email": "111@qq.com", "workId": 11}
# user = dect({"email": "111@qq.com", "workId": 11})
# user = {"email": "111@qq.com", "workId": 11, "workId": 10}
user1 = {"email": "111@qq.com", "workId": 11, (11, 1101): "Floor&Room"}
# user1 = {"email": "111@qq.com", "workId": 11, [11, 1101]: "Floor&Room"}
print(user1)

print(user.keys())
print(user.values())
print("email" in user)

user["email"] = "222@qq.com"
print(user["email"])

user["address"] = "BeiJing"
user.update({"name": "px"})
print(user)

del user["address"]
print(user)

user.clear()
print(user)

del user
# print(user)
