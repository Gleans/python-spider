import os
import requests
from lxml import etree
import re
import time
import urllib.request

target_path = "D:/spider/maijiaxiu/"  # 注意更改你锁需要存放的路径，否则会报错

majwxq_url = "http://www.qipamaijia.com/fuli/"


def save_file(paths):
    for path in paths:
        path_fmt = re.findall(r"https://img.qipamaijia.com/Images/(.*)", path, flags=re.IGNORECASE)
        if path_fmt:
            path_temp = path_fmt[0]
            try:
                path_address = path_temp.replace("/", "-")
                filename = '{}{}'.format(target_path, path_address)
                if not os.path.exists(filename):
                    print(filename)
                    urllib.request.urlretrieve(path, filename=filename)  # 利用urllib.request.urltrieve方法下载图片
                    time.sleep(1)
            except IOError as e:
                print(1, e)
            except Exception as e:
                print(2, e)


def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/60.0.3112.113 Safari/537.36'
    }

    return requests.get(url=url, headers=headers)


def get_total_pages(url):
    response = get_data(url)

    xpath = '//span[@class="dots"]/following-sibling::a[1]/text()'

    wb_data = response.text  # 将页面转换成文档树
    html = etree.HTML(wb_data)
    text = html.xpath(xpath)[0]

    print("===========================获取到一共" + str(text) + "页")

    return text


def find_pictures(url):
    response = get_data(url)

    print("请求的网址：" + str(url))

    wb_data = response.text  # 将页面转换成文档树
    html = etree.HTML(wb_data)

    return html.xpath('//img[@class="lazy"]/@src')


init_page = 1
total_pages = int(get_total_pages(url=majwxq_url))
for i in range(init_page, total_pages):
    pics = find_pictures(majwxq_url + str(i))
    time.sleep(1)
    save_file(pics)
