import urllib
from urllib import request

# resp = request.urlopen('http://www.baidu.com')
# print(resp.read().decode())

# resp = request.urlopen('http://httpbin.org', data=b'word=hello', timeout=10)
# print(resp.read().decode())


url = 'http://www.baidu.com/s'
keyword = input("请输入字符串：")
wd = {"wd": keyword}
wd = urllib.parse.urlencode(wd)
fullurl = url + "?" + wd
print(fullurl)

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

req = request.Request(fullurl, headers=headers)
resp = request.urlopen(req)
print(resp.read().decode())
print(resp.getcode())
print(resp.geturl())
print(resp.info())

