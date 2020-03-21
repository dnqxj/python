from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os


url = 'www'

def start_chrome():
    driver = webdriver.Chrome(executable_path=r'C:\Users\dnqxz\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    driver.start_client()
    return driver

def find_info():
    sel = '.t.c-gap-bottom-small > a'
    elements = driver.find_elements_by_css_selector(sel)
    return elements



driver = start_chrome()
driver.get('https://www.baidu.com')
time.sleep(1)
driver.find_element_by_id('kw').send_keys('hello worlds')
time.sleep(1)
driver.find_element_by_id('su').click()
time.sleep(1)

elements = find_info()
# 访问查询结果的第一个
elements[0].click()
