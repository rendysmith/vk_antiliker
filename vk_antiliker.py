# -*- coding: cp1251 -*-
import random
from selenium import webdriver
#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import os
import sys

import threading
import requests

vk_url = "https://vk.com/feed?section=likes"

cor_path = os.path.abspath(os.curdir)
print(cor_path)

opt = webdriver.ChromeOptions()
opt.add_argument("start-minimized")
#opt.add_argument(fr"user-data-dir={cor_path}/Kontur")
opt.add_argument(fr"user-data-dir={cor_path}/vk")
#exec_path = cor_path + "/chromedriver.exe"
exec_path = cor_path + '/chromedriver.exe'

s = Service(exec_path)

def page_down(browser):
    page = browser.find_element(By.TAG_NAME, "html")
    for i in range(3):
        page.send_keys(Keys.END)
        time.sleep(0.5)

def get_likes():
    #browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser = webdriver.Chrome(service=s, options=opt)
    #browser = webdriver.Chrome(options=opt)
    browser.set_window_size(500, 500)  # Ширина высота
    browser.get(vk_url)

    n = 1
    while True:
        try:
            likes = browser.find_elements(By.CSS_SELECTOR, "div[class='PostBottomAction PostBottomAction--withBg PostButtonReactions PostButtonReactions--post PostButtonReactions--icon-active PostButtonReactions--active']")
            print('Len Likes in Note =', len(likes))

            if len(likes) == 0:
                likes = browser.find_elements(By.CSS_SELECTOR, "div[class='PostBottomAction PostBottomAction--withBg like _like active']")
                print('Len Likes Com =',len(likes))

            if len(likes) > 0:
                for like in likes:
                    like.click()
                    time_r = random.randint(2, 7)
                    time_r = random.uniform(0, 2)
                    #time_r = 0.5
                    time.sleep(time_r)

                    print(f'+++ {n} Click! Wait {time_r:.2f} sec.')
                    n += 1

                # for i in range(1):
                #     likes[-1].send_keys(Keys.END)
                #     print('- Send Key END')
                #     time.sleep(1)

            else:
                time.sleep(1)
                print('Wait!')
                                             #'PostBottomAction PostBottomAction--withBg PostButtonReactions PostButtonReactions--post'
        except:
            print('--- Error. ---')
            try:
                box = browser.find_element(By.CSS_SELECTOR,
                                              "div[class='box_x_button']")
                box.click()
                print('Close box!')

            except:
                time.sleep(5)


            n = 1


get_likes()


def selenium_start():

    code = 0
    while code != 200:
        try:
            r = requests.get(kontur_url)
            code = r.status_code
            print('Status code OK,', code)
        except:

            print('Status code', code)
            time.sleep(5)

    start_th = threading.active_count()
    list_names = get_names()

    for k, name in enumerate(list_names):
        #print(f'\n{k} {name}')
        threading.Thread(target=get_excel, args=(k, name,)).start()
        #get_excel(name)
        time.sleep(15)

        #input()

        while threading.active_count() > 5:
            print(f'Threading active count = {threading.active_count()}')
            time.sleep(5)

    n = 1
    while start_th != threading.active_count():
      print(f'Кол-во потоков = {threading.active_count()}')
      time.sleep(5)
      n += 1

      if n > 720:
        print('STOP BOT!')
        break
