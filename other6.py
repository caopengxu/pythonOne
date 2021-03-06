from multiprocessing import Pool
import time
import os


def test():
    print("--pid=%d,ppid=%d" % (os.getpid(), os.getppid()))
    for i in range(3):
        print("--%d--" % i)
        time.sleep(1)
    return "haha"


def test2(args):
    print("--%d" % os.getpid())
    print("--%s" % args)


pool = Pool(3)
pool.apply_async(func=test, callback=test2)

time.sleep(5)

print("---主进程-pid-%d---" % os.getpid())
