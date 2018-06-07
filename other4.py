from threading import Thread, Lock

g_num = 0


def test1():
    global g_num
    for i in range(1000000):
        lock.acquire()
        g_num += 1
        lock.release()
    print("test1--%d" % g_num)


def test2():
    global g_num
    for i in range(1000000):
        lock.acquire()
        g_num += 1
        lock.release()
    print("test2--%d" % g_num)


lock = Lock()

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()
