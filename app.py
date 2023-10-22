from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import keyboard
import json
import codecs

set_options = Options()
#背景執行
#set_options.add_argument('--headless')
#指定瀏覽器解析度 
#set_options.add_argument('window-size=1920x1000')
#啟動就最大化
set_options.add_argument('--start-maximized')
#不加載圖片, 提升速度
set_options.add_argument('blink-settings=imagesEnabled=false') 
#以最高權限運行
set_options.add_argument('--no-sandbox')
#加上這個屬性來規避bug
set_options.add_argument('--disable-gpu')
#關閉chrome 通知
set_options.add_argument("--disable-notifications")
#去除錯誤
set_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#不關閉瀏覽器
set_options.add_experimental_option("detach", True)
#取得參數
config = json.load(open('config.json', 'r'))

#放入要重複執行的程式碼    
chrome = webdriver.Chrome(options=set_options)
chrome.get("https://www.facebook.com")

#抓取元素  定義元素
email = chrome.find_element(By.NAME,"email")
password = chrome.find_element(By.NAME,"pass")
btn_clcik = chrome.find_element(By.NAME,"login")

#填入值
email.send_keys(config["fb"]["username"])
password.send_keys(config["fb"]["password"])

#使用按鈕按下去方法
btn_clcik.click()

#暫停五秒 讓他轉頁過去
time.sleep(5)

#抓取元素  定義元素
search_text = chrome.find_element(By.XPATH, "//input[@type='search']")
#填入值
search_text.send_keys("台北市")
#按enter
search_text.send_keys(Keys.ENTER)

#暫停五秒 讓他轉頁過去
time.sleep(5)

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            chrome.quit()
            break  # finishing the loop
        else:
            #捲動貼文 每次移動Y軸1000像素
            chrome.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            text_file = codecs.open('html.txt', "w", "utf-8")
            text_file.write(chrome.page_source)
            text_file.close()
            #暫停5秒
            time.sleep(5)
    except:
        break  # if user pressed a key other than the given key the loop will break

#關閉分頁
#chrome.close()    
#關閉瀏覽器 
#chrome.quit()   
