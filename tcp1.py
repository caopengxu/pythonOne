import socket
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(("", 6789))
serverSocket.listen(1000)


def main():
    while 1:
        clientSocket, clientAddress = serverSocket.accept()
        print("%s, %s 用户已连接" % clientAddress)
        handleClientProcess = Process(target=handleClient, args=(clientSocket,))
        handleClientProcess.start()
        clientSocket.close()


def handleClient(clientSocket):
    requestData = clientSocket.recv(1024)
    print("*" * 20)
    print("----%s" % requestData)

    requestLines = requestData.splitlines()
    for line in requestLines:
        print("*" * 10)
        print(line)
    requestStartLine = requestLines[0]
    fileName = re.match(r"\w+ +(/[^ ]*) ", requestStartLine.decode("utf-8")).group(0)
    print("*" * 20)
    print(fileName)

    if "/" == fileName
        fileName = "/index.html"

    try:
        # file = open(HTML_ROOT_DIR + fileName, "rb")
        file = open(HTML_ROOT_DIR + "/index.html", "rb")
    except IOError:
        responseStartLine = "HTTP/1.1 404 Not Found\r\n"
        responseHeaders = "Server: My server\r\n"
        responseBody = "not found"
    else:
        fileData = file.read()
        file.close()

        responseStartLine = "HTTP/1.1 200 OK\r\n"
        responseHeaders = "Server: My server\r\n"
        responseBody = fileData.decode("utf-8")
    finally:
        response = responseStartLine + responseHeaders + "\r\n" + responseBody
        print("*"*20)
        print(response)

    clientSocket.send(bytes(response, "utf-8"))
    clientSocket.close()


if __name__ == '__main__':
    main()
