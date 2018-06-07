num = 2

if num < 10:
    content = "{0} is less than 10".format(num)
    print(content)
elif 10 < num < 20:
    # elif num > 10 and num < 20:
    # elif num == 10 or num == 20:
    print("10-20")
elif num not in [10, 20]:
    print("!=10 or 20")
else:
    print("20--")

if not "":
    print("123")
if not ():
    print("123")
if not []:
    print("123")
if not None:
    print("123")

if __name__ == "__main__":
    print("999")

# -------------------------------------------------
for num in range(1, 4):
    # if num == 2:
    #     break
    print(num)
else:
    print("end")

user = {"email": "123@qq.com", "name": "px"}
for info in user:
    print(info)
    print(user[info])

a = 1
while a < 10:
    if a % 2 == 0:
        a += 1
        continue

    print(a)
    a += 1
