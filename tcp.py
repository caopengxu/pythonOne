from socket import *
from multiprocessing import Process


so = socket(AF_INET, SOCK_STREAM)

# so.bind(("", 4567))
# so.listen(5)
#
# clientSocket, clientInfo = so.accept()
#
# recvData = clientSocket.recv(1024)
#
# print("%s:%s" % (str(clientInfo), recvData))
#
# clientSocket.close()
# so.close()


so.connect(("10.211.55.4", 4567))
so.send("haha".encode("gb2312"))
recvData = so.recv(1024)

print("recvData%s" % recvData)

so.close()


serSocket = socket(AF_INET, SOCK_STREAM)
serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serSocket.bind(("", 7788))
serSocket.listen(5)

def main():

try:
    while 1:
        newSocket, destAddr = serSocket.accept()
        client = Process(target=dea, args=sd)






if __name__ == '__main__':
    main()

