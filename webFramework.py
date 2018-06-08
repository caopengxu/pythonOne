import time

HTML_ROOT_DIR = "./html"


class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, startResponse):
        path = env.get("PATH_INFO", "/")

        if path.startswith("/static"):
            fileName = path[7:]

            try:
                file = open(HTML_ROOT_DIR + fileName, "rb")
            except IOError:
                status = "404 Not Found"
                headers = []
                startResponse(status, headers)
                return "not found"

                # responseStartLine = "HTTP/1.1 404 Not Found\r\n"
                # responseHeaders = "Server: My server\r\n"
                # responseBody = "not found"
            else:
                fileData = file.read()
                file.close()

                status = "200 OK"
                headers = []
                startResponse(status, headers)
                return fileData.decode("utf-8")

                # responseStartLine = "HTTP/1.1 200 OK\r\n"
                # responseHeaders = "Server: My server\r\n"
                # responseBody = fileData.decode("utf-8")

        for url, handler in self.urls:
            if path == url:
                return handler(env, startResponse)

        status = "404 Not Found"
        headers = []
        startResponse(status, headers)
        return "not found"


def show_ctime(env, startResponse):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    startResponse(status, headers)
    return time.ctime()


def hello(env, startResponse):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    startResponse(status, headers)
    return "hello"


urls = [
        ("/", show_ctime),
        ("/ctime", show_ctime),
        ("/index.html", hello)
    ]

app = Application(urls)
