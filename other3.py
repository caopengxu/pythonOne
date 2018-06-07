# import os
import time
from multiprocessing import Process
import random

# ret = os.fork()
#
# if ret == 0:
#     while 1:
#         print("0")
#         time.sleep(1)
# else:
#     while 1:
#         print("1")
#         time.sleep(1)

for i in range(random.randint(1, 5)):
    print("--%d---" % i)
    time.sleep(1)


def test():
    while 1:
        print("123")
        time.sleep(1)


p = Process(target=test)
p.start()

while 1:
    print("main")
    time.sleep(1)
