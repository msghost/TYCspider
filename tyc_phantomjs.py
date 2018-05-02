from selenium import webdriver
import time
# path = r'C:\Users\G\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# browser = webdriver.PhantomJS(path)
browser = webdriver.Chrome()

browser.get('https://www.tianyancha.com/')
time.sleep(2)
browser.find_element_by_link_text('登录/注册').click()
time.sleep(1)
browser.find_element_by_xpath('//div[text()="账号密码登录"]').click()
time.sleep(1)
user_input = browser.find_element_by_xpath('.//div[@class="bgContent"]/div[@class="module module1 module2 loginmodule collapse in"]/div[@class="modulein modulein1 mobile_box pl15 pr15 f14 collapse in"]/div[@class="pb30 position-rel"]/input[@class="_input input_nor contactphone"]')
user_input.send_keys(13521392470)
time.sleep(1)
pwd_input = browser.find_element_by_xpath('.//div[@class="bgContent"]/div[@class="module module1 module2 loginmodule collapse in"]/div[@class="modulein modulein1 mobile_box pl15 pr15 f14 collapse in"]/div[@class="pb40 position-rel"]/input[@class="_input input_nor contactword"]')
pwd_input.send_keys('admin123')
browser.find_element_by_xpath('.//div[@class="bgContent"]/div[@class="module module1 module2 loginmodule collapse in"]/div[@class="modulein modulein1 mobile_box pl15 pr15 f14 collapse in"]/div[@class="c-white b-c9 pt8 f18 text-center login_btn"]').click()
for class_name in browser.find_element_by_xpath('.//a[@class="c3 search-detail"]'):
    print(class_name)