import urllib
from urllib import request
import codecs
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


def loadPage(url, filename):
    print("正在下载" + filename)

    # headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    # req = request.Request(url, headers=headers)

    print(url)
    resp = request.urlopen(url)
    return resp.read().decode("utf-8")


def writePage(html, filename):
    print("正在保存" + filename)

    filename = "/Users/cpx/Desktop/" + filename
    fp = codecs.open(filename, "w", "utf-8")
    fp.write(html)
    fp.close()

    # with open(filename, "w") as f:
    #     f.write(html)
    print("*"*30)


def tiebaSpider(url, begin_page, end_page):
    for page in range(begin_page, end_page):
        pn = (page - 1)*50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)

        html = loadPage(fullurl, filename)
        writePage(html, filename)
        print("谢谢使用")


if __name__ == "__main__":
    kw = input("请输入贴吧名：")
    begin_page = int(input("请输入起始页："))
    end_page = int(input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, begin_page, end_page)
