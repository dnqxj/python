
"""
    目的
        - 访问某人微信某时间段内所有微博信息，抓取发布时间，微博链接，内容
        - 访问鞠婧祎 微博数据，并下载图片
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os
import requests


# url = 'https://weibo.com/bgsxy?is_ori=1&key_word=*&start_time=2017-01-18&end_time=2020-03-21&is_search=1&is_searchadv=1#_0'
img_output = './imgs/'
if not os.path.exists(img_output):
    os.makedirs(img_output)

def save_img(url, img_filename):
    # 这是一个图片的url
    response = requests.get(url)
    # 获取的文本实际上是图片的二进制文本
    img = response.content
    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    with open(img_output + img_filename, 'wb') as f:
        f.write(img)


def start_chrome():
    driver = webdriver.Chrome(executable_path=r'C:\Users\dnqxz\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    driver.start_client()
    return driver

def q(st, et):
    return f'?is_ori=1&key_word=*&start_time={st}&end_time={et}&is_search=1&is_searchadv=1#_0'

def scroll_down():
    html_page = driver.find_element_by_tag_name('html')
    for i in range(8):
        print(i)
        html_page.send_keys(Keys.END)
        time.sleep(0.6)

def find_cards_info():
    cards_sel = 'div.WB_feed_like'
    cards = driver.find_elements_by_css_selector(cards_sel)
    info_list = []
    img_list = []

    for card in cards:
        content_sel = 'div.WB_text.W_f14'
        time_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'
        link_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'
        # 点赞量
        start_sel = 'div.WB_feed_handle ul li:nth-child(4) > a > span > span > span > em:nth-child(2)'
        # img_sel
        img_sel = 'div.WB_media_wrap img'

        content = card.find_element_by_css_selector(content_sel).text
        date = card.find_element_by_css_selector(time_sel).get_attribute('title')
        link = card.find_element_by_css_selector(link_sel).get_attribute('href')
        start = card.find_element_by_css_selector(start_sel).text

        img_elements = card.find_elements_by_css_selector(img_sel)
        # 图片下载，会耗费大量时间
        # if img_elements:
        #     for img in img_elements:
        #         img_href = img.get_attribute('src')
        #         if img_href:
        #             # 处理图片链接
        #             img_href = img_href.replace("thumb150", "mw690");
        #             img_href = img_href.replace("orj360", "mw690");
        #             img_href = img_href.replace("orj480", "mw690");
        #
        #             time.sleep(0.3)
        #             # 处理img后的?
        #             img_filename = img_href.split('?')[0]
        #             img_filename = img_filename.split('/')[-1]
        #             save_img(img_href, img_filename)
        #             img_list.append(img_href)

        info_list.append([date, link, content, start])
    return info_list, img_list

# 下一页
def next_page():
    next_sel = 'a.page.next.S_txt1.S_line1'
    next_btn = driver.find_elements_by_css_selector(next_sel)
    if next_btn:
        return next_btn[0].get_attribute('href')
    else:
        return

def save(info_list, name):
    full_path = './' + name + '.csv'
    if os.path.exists(full_path):
        with open(full_path, 'a', encoding = 'utf8') as f:
            writer = csv.writer(f)
            writer.writerows(info_list)
    else:
        with open(full_path, 'w+', encoding = 'utf8') as f:
            writer = csv.writer(f)
            writer.writerows([['date', 'link', 'content', 'start']])
            writer.writerows(info_list)


def run_crawler(href, filename):
    driver.get(href)
    time.sleep(5)
    scroll_down()
    time.sleep(5)
    info_list, img_list = find_cards_info()
    save(info_list, filename)
    save(img_list, 'img_list_src')
    next_href = next_page()
    if next_href:
        run_crawler(next_href, filename)


start_time = '2019-01-01'
end_time = '2020-03-03'

base_url = 'https://weibo.com/bgsxy'
# 鞠婧祎
base_url = 'https://weibo.com/u/3669102477'
name = '鞠婧祎'
driver = start_chrome()
driver.get(base_url)
print('login in weibo')

# 登录
print('input anything to start')
input()
start_href = base_url + q(start_time, end_time)
run_crawler(start_href, str(name) + str(start_time) + '~' + str(end_time))

