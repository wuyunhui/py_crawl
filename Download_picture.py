import os
import re
import requests
from urllib.parse import urljoin

def url_open(url):
#定义模拟浏览器，返回网页请求
    headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    response = requests.get(url, headers=headers)
    return response

def find_imgs(url):
#查找返回网页请求里的图片源码
    html = url_open(url).text
    p = r'<img src="([^"]+\.jpg)"'
    img_address = re.findall(p, html)

#遍历列表img_address0到x号元素
    for each in img_address[0:x]:
        img = urljoin("http:", each)    #构造绝对地址
        print(img)
        path = root + img.split('/')[-1]

        try:
            if not os.path.exists(path):
                r = requests.get(img)
                print(r.text)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("保存成功")
            else:
                print("文件已存在")
        except:
            print("目录已存在")

if __name__ == '__main__':
#    url = input("下载图片地址")
#    root = input("文件贮存目录") + "/"
    x = int(input("下载数量"))

    url = "https://www.ivsky.com/"
    root = "C:\\Users\\23691\\Pictures\\联想锁屏壁纸\\"


    find_imgs(url)
    print("关注公众号：不正经的化工人，获取源码")