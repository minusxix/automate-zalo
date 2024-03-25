from selenium import webdriver
from selenium.common import NoSuchElementException
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

time.sleep(15)

new = browser.find_element(By.XPATH, '//i[@class="fa fa-outline-add-new-contact-2 pre"]').click()

time.sleep(2)

#ko tìm thấy
phone = browser.find_element(By.XPATH, '//input[@class="phone-i-input flx-1"]').send_keys('0766661910')

time.sleep(2)

search = browser.find_element(By.XPATH, '//div[@class="z--btn--v2 btn-primary large  --rounded"]').click()

time.sleep(2)

chat = browser.find_element(By.XPATH, '//div[@class="z--btn--v2 btn-secondary medium  --full-width"]').click()

time.sleep(2)

input = browser.find_element(By.XPATH, '//div[@id="input_line_0"]')
input.click()
input.send_keys('Testing project!')

time.sleep(2)

send = browser.find_element(By.XPATH, '//i[@class="fa fa-Sent-msg_24_Line pre"]').click()

time.sleep(2)

try:
    add = browser.find_element(By.XPATH, '//div[@class="z--btn--v2 btn-neutral small  --rounded"]')
    add.click()
    time.sleep(2)
    accept = browser.find_element(By.XPATH, '//div[@class="z--btn--v2 btn-primary large  --rounded"]')
    accept.click()
except NoSuchElementException:
    print('Đã kết bạn!')

time.sleep(30)
