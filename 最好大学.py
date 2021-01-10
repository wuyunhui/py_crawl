import requests
from bs4 import BeautifulSoup as bs
import bs4


def GetHtml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def FillUni(ulist, html):
    soup = bs(html, "html.parser")
    for tr in soup.find('table').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])
    return ulist


def PrintList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    for i in range(0, num):
        uni = ulist[i]
        print(tplt.format(uni[0], uni[1], uni[2], chr(12288)))


def Paiming():
    uinfo = []
    url = 'https://www.eol.cn/e_html/gk/dxpm/index.shtml'
    html = GetHtml(url)
    FillUni(uinfo, html)
    num = int(input("你想获得前多少所学校排名呢？\n"))
    PrintList(uinfo, num)


def Find():
    uinfo = []
    url = 'https://www.eol.cn/e_html/gk/dxpm/index.shtml'
    html = GetHtml(url)
    ulist = FillUni(uinfo, html)
    sch = input("你想知道哪所学校的排名？\n")
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    for i in range(1, 500):
        if ulist[i]:
            uni = ulist[i]
            if sch == uni[1]:
                print(tplt.format(uni[0], uni[1], uni[2], chr(12288)))
            elif i == 499:
                print("未找到该学校")


if __name__ == '__main__':
    fun = input("输入1获得部分高校排名，输入其他数字获得特定高校排名！\n")
    fun = int(fun)
    if fun == 1:
        Paiming()
    else:
        Find()
    print("该排名来自——中国教育在线")
    print("关注公众号：不正经的化工人，获取源码")
    input("任意输入结束程序\n")
