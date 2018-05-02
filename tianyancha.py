import json
import time
import requests
from lxml import etree
import random
from selenium import webdriver

class TycSpider(object):
    """docstring for TycSpider"""
    def __init__(self):
        self.first_url = 'https://www.tianyancha.com/'   
        # path = r'C:\Users\G\Desktop\phantomjs2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe'
        # self.browser = webdriver.PhantomJS(path)
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.tianyancha.com/')
        time.sleep(2)
        self.browser.find_element_by_link_text('登录/注册').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//div[text()="账号密码登录"]').click()
        time.sleep(1)
        user_input = self.browser.find_element_by_xpath('.//div[@class="bgContent"]/div[@class="module module1 module2 loginmodule collapse in"]/div[@class="modulein modulein1 mobile_box pl15 pr15 f14 collapse in"]/div[@class="pb30 position-rel"]/input[@class="_input input_nor contactphone"]')
        user_input.send_keys(13521392470)
        time.sleep(1)
        pwd_input = self.browser.find_element_by_xpath('.//div[@class="bgContent"]/div[@class="module module1 module2 loginmodule collapse in"]/div[@class="modulein modulein1 mobile_box pl15 pr15 f14 collapse in"]/div[@class="pb40 position-rel"]/input[@class="_input input_nor contactword"]')
        pwd_input.send_keys('admin123')
        self.browser.find_element_by_xpath('.//div[@class="bgContent"]/div[@class="module module1 module2 loginmodule collapse in"]/div[@class="modulein modulein1 mobile_box pl15 pr15 f14 collapse in"]/div[@class="c-white b-c9 pt8 f18 text-center login_btn"]').click()
        self.base_html = self.browser.page_source
    def hanlder_request(self,url):
        self.browser.find_element_by_xpath('.//a[@href=%s]'%url).click()
        time.sleep(2)
        print(self.browser.page_source)
        html = etree.HTML(self.browser.page_source)
        return html

    def parse_class_url(self,xpath_obj):

        class_name = xpath_obj.xpath('.//a[@class="c3 search-detail"]/text()')
        class_url = xpath_obj.xpath('.//a[@class="c3 search-detail"]/@href')
        dict1 = dict(zip(class_name,class_url))
        self.url_dict = dict1
        print(dict1)
        return dict1

    def parse_comp_name(self,xpath_obj):
        comp_name = xpath_obj.xpath('.//a[starts-with(@class,"query_name")]/span/text()')
        self.comp_name_list.extend(comp_name)
        print(comp_name)
        print(self.comp_name_list)
        next_url = xpath_obj.xpath('.//li[starts-with(@class,"pagination-next")]/a[@class="ng-binding"]/@href')
        time.sleep(5)
        if len(next_url)>0:
            xpath_obj = self.hanlder_request(next_url[0])
            self.parse_comp_name(xpath_obj)

    def crawl(self):
        xpath_obj = etree.HTML(self.base_html)
        class_dict = self.parse_class_url(xpath_obj)
        class_comp_dict = {}
        for k,v in class_dict.items():
            self.comp_name_list = []
            xpath_obj = self.hanlder_request(v)
            self.parse_comp_name(xpath_obj)
            class_comp_dict[k] = self.comp_name_list
            time.sleep(5)
        print(class_comp_dict)
        with open('./comp_class.json','w',encoding='utf-8') as fp:
            string1 = json.dumps(self.url_dict,ensure_ascii=False)
            string2 = json.dumps(class_comp_dict,ensure_ascii=False)
            fp.write(string1+'\n'+string2)



t = TycSpider()
t.crawl()