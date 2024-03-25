from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = Options()

import time

path = r"C:\Users\kidfa\Desktop\Auto\chromedriver.exe" #123
ser = Service(path)
browser = webdriver.Chrome(service=ser)
browser.get('https://chat.zalo.me/')
browser.maximize_window()

time.sleep(30)

