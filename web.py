import socket
from multiprocessing import Process
import re
import sys

HTML_ROOT_DIR = "./html"


class HTTPServer(object):
    def __init__(self, app):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = app

    def bind(self, port):
        self.serverSocket.bind(("", port))

    def start(self):
        self.serverSocket.listen(1000)
        while 1:
            clientSocket, clientAddress = self.serverSocket.accept()
            process = Process(target=self.handleClient, args=(clientSocket, ))
            process.start()
            clientSocket.close()

    def startResponse(self, status, headers):
        responseHeaders = "HTTP/1.1" + status + "\r\n"
        for header in headers:
            responseHeaders += "%s: %s\r\n" % header
        self.responseHeaders = responseHeaders

    def handleClient(self, clientSocket):
        requestData = clientSocket.recv(1024)
        requestLines = requestData.splitlines()
        requestStartLine = requestLines[0]
        print(requestStartLine.decode("utf-8"))
        fileName = re.match(r"\w+ +(/[^ ]*) ", requestStartLine.decode("utf-8")).group(1)
        method = re.match(r"(\w+) +/[^ ]* ", requestStartLine.decode("utf-8")).group(1)

        env = {
            "PATH_INFO": fileName,
            "METHOD": method
        }
        responseBody = self.app(env, self.startResponse)
        response = self.responseHeaders + "\r\n" + responseBody

        clientSocket.send(bytes(response, "utf-8"))
        clientSocket.close()


def main():
    sys.path.insert(1, HTML_ROOT_DIR)
    if len(sys.argv) < 2:
        sys.exit("framework!!!")

    moduleName, appName = sys.argv[1].split(":")
    m = __import__(moduleName)
    app = getattr(m, appName)
    httpServer = HTTPServer(app)
    httpServer.bind(4567)
    httpServer.start()


if __name__ == '__main__':
    main()
