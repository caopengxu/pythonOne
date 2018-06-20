import urllib.request

# http_handler = urllib.request.HTTPHandler()
http_handler = urllib.request.HTTPHandler(debuglevel=1)
https_handler = urllib.request.HTTPSHandler()

opener = urllib.request.build_opener(http_handler)
request = urllib.request.Request("http://www.baidu.com")
response = opener.open(request)

# print(response.read().decode("utf-8"))


proxy_switch = True
http_proxy_handler = urllib.request.ProxyHandler({"https": "58.221.72.185:3128"})
null_proxy_handler = urllib.request.ProxyHandler({})

if proxy_switch:
    opener_proxy = urllib.request.build_opener(http_proxy_handler)
else:
    opener_proxy = urllib.request.build_opener(null_proxy_handler)

urllib.request.install_opener(opener_proxy)
request_proxy = urllib.request.Request("https://www.baidu.com")
response_proxy = urllib.request.urlopen(request_proxy)

print(response_proxy.read().decode("utf-8"))
