import requests
from lxml import etree
import time
# 通过Session类新建一个会话
session = requests.Session()
post_url = 'https://www.tianyancha.com/cd/login.json'
# 往下使用requests的地方，直接使用session即可，session就会保存服务器发送过来的cookie信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Referer': 'https://www.tianyancha.com',
    'Cookie': 'TYCID=f183e8a04a9011e8ac23b7b979814074; undefined=f183e8a04a9011e8ac23b7b979814074; ssuid=1547602646; aliyungf_tc=AQAAAFjY9x1UDwUASoPNfKQBwrmOU74o; csrfToken=EDHSrep2UvGUzJ3LNW7-CqNd; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1524884704,1524886349,1525222713,1525231486; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1525231589; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzUyMTM5MjQ3MCIsImlhdCI6MTUyNTIzMTUwOSwiZXhwIjoxNTQwNzgzNTA5fQ.pPfpkLeZsHYKpd1U8h7ekYRNWpbYcz_3okBX0xYR4b7wUI2E5YUmsNfgS8G1p1UeBJJu9KXtpYCTBwk6YjO2YA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25224%2522%252C%2522surday%2522%253A%25227%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213521392470%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzUyMTM5MjQ3MCIsImlhdCI6MTUyNTIzMTUwOSwiZXhwIjoxNTQwNzgzNTA5fQ.pPfpkLeZsHYKpd1U8h7ekYRNWpbYcz_3okBX0xYR4b7wUI2E5YUmsNfgS8G1p1UeBJJu9KXtpYCTBwk6YjO2YA'

}
data = {"mobile":"13521392470","cdpassword":"0192023a7bbd73250516f069df18b500","loginway":"PL","autoLogin":"true"}

r = session.post(url=post_url, data=data, headers=headers,verify=False)

# 上面的session会保存会话，往下发送请求，直接使用session即可
url = 'https://www.tianyancha.com/'

rp = session.get(url=url, headers=headers,verify=False)
with open('response.html','w',encoding='utf-8') as fp:
    fp.write(rp.text)
xpath_obj = etree.HTML(rp.text)
class_name = xpath_obj.xpath('.//a[@class="c3 search-detail"]/text()')
class_url = xpath_obj.xpath('.//a[@class="c3 search-detail"]/@href')
dict1 = dict(zip(class_name,class_url))
url_dict = dict1
print(dict1)
class_comp_dict = {}
def parse_comp(class_url,cok=rp.cookies):
    
    r = session.get(url=class_url, headers=headers,cookies=cok,verify=False)
    with open('response1.html','w',encoding='utf-8') as fp:
        fp.write(r.text)
    xpath_obj = etree.HTML(r.text)
    comp_name = xpath_obj.xpath('.//a[starts-with(@class,"query_name")]/span/text()')
    comp_name_list.extend(comp_name)
    print(comp_name_list)
    next_url = xpath_obj.xpath('.//li[starts-with(@class,"pagination-next")]/a[@class="ng-binding"]/@href')
    time.sleep(5)
    if len(next_url)>0:
        parse_comp(xpath_obj,cok=r.cookies)


for k,v in dict1.items():
    comp_name_list = []
    parse_comp(v)
    class_comp_dict[k] = comp_name_list
    time.sleep(5)
with open('./comp_class.json','w',encoding='utf-8') as fp:
    string1 = json.dumps(url_dict,ensure_ascii=False)
    string2 = json.dumps(class_comp_dict,ensure_ascii=False)
    fp.write(string1+'\n'+string2)


