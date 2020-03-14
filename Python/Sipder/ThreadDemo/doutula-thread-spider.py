import requests
import re
import os
from lxml import etree
from urllib import request
from queue import Queue
import threading


class Producer(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_url(url)

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath(
            "//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?\.？。！!\*]', '', alt)
            # 取后缀名
            suffix = os.path.splitext(img_url)[1]
            img_name = alt + suffix
            # request.urlretrieve(img_url,'images/'+img_name)
            # print(img_name)
            self.img_queue.put((img_url, img_name))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, img_name = self.img_queue.get()
            request.urlretrieve(img_url, 'images/'+img_name)
            print("download finish!%s" % img_name)


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(100):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue, img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == "__main__":
    main()
