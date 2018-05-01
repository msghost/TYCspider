import json
import time
import requests
from lxml import etree

class TycSpider(object):
    """docstring for TycSpider"""
    def __init__(self):
        self.first_url = 'https://www.tianyancha.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537'
            
        }


    def hanlder_request(self,url):
        response = requests.get(url=url,headers=self.headers)
        with open('response.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
        html = etree.HTML(response.text)
        return html

    def parse_class_url(self,xpath_obj):

        class_name = xpath_obj.xpath('.//a[@class="c3 search-detail"]/text()')
        class_url = xpath_obj.xpath('.//a[@class="c3 search-detail"]/@href')
        dict1 = dict(zip(class_name,class_url))
        # print(dict1)
        return dict1

    def parse_comp_name(self,xpath_obj):
        comp_name = xpath_obj.xpath('.//a[@class="query_name sv-search-company f18 in-block vertical-middle"]/span[@class="select-none"]/text[@class="tyc-num"]/text()')
        self.comp_name_list.extend(comp_name)
        print(comp_name)
        next_url = xpath_obj.xpath('.//ul[@class="pagination-sm pagination pt20"]/li[@class="pagination-next ng-scope "]/a[@class="ng-binding"]/@href')
        time.sleep(1)
        if len(next_url)>0:
            xpath_obj = self.hanlder_request(next_url)
            self.parse_comp_name(xpath_obj)

    def crawl(self):
        xpath_obj = self.hanlder_request(self.first_url)
        class_dict = self.parse_class_url(xpath_obj)
        class_comp_dict = {}
        for k,v in class_dict.items():
            self.comp_name_list = []
            xpath_obj = self.hanlder_request(v)
            self.parse_comp_name(xpath_obj)
            class_comp_dict[k] = self.comp_name_list
            time.sleep(1)
        print(class_comp_dict)



t = TycSpider()
t.crawl()