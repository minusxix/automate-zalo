from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = Options()

import time
import xlwings as xw

path = r"C:\Users\kidfa\Desktop\Auto\chromedriver.exe" #123
ser = Service(path)
browser = webdriver.Chrome(service=ser)
browser.get('https://chat.zalo.me/')
browser.maximize_window()

time.sleep(15)

range = xw.Range('A1:A3').value
for num in range:
    if num is None or num.strip() == '':
        continue
    time.sleep(2)
    new = browser.find_element(By.XPATH, '//i[@class="fa fa-outline-add-new-contact-2 pre"]').click()
    time.sleep(2)
    try:
        phone = browser.find_element(By.XPATH, '//input[@class="phone-i-input flx-1"]').send_keys(num)
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

    except NoSuchElementException:
        print('Không tìm thấy!')
        cancel = browser.find_element(By.XPATH, '//i[@class="fa fa-close f16 pre"]').click()
        continue

time.sleep(30)
