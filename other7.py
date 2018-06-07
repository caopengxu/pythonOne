from socket import *
from threading import Thread


# tcp
s = socket(AF_INET, SOCK_STREAM)
# udp
s1 = socket(AF_INET, SOCK_DGRAM)

# sendAddr = ("192.168.1.103", 8080)
# s1.sendto("haha", ("192.168.0.186", 7788))
# s1.sendto("hehe".encode("utf-8"), ("192.168.0.186", 7788))
# s1.sendto("hehe".encode("gb2312"), ("192.168.0.186", 7788))

s1.bind(("", 7788))
recvData = s1.recvfrom(1024)
print(recvData)

# a, b = recvData
# print("%s" % a)
# print("%s" % a.encode("utf-8"))


def recvData():
    while 1:
        recvInfo = udpSocket.recvfrom(1024)
        print(">>%s:%s" % (str(recvInfo[1]), recvInfo[0]))


def sendData():
    while 1:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode("utf-8"), (destIp, destPort))


udpSocket = socket(AF_INET, SOCK_DGRAM)
destIp = ""
destPort = 0


def main():
    global destIp
    global destPort

    destIp = input("对方IP:")
    destPort = input("对方端口:")

    udpSocket.bind("", 4567)

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()


if __name__ == "__main__":
    main()
