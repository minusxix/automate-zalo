import webbrowser
import tkinter as tk
from tkinter import filedialog, ttk
import shutil
import os
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import xlwings as xw


def copy_and_open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        destination_folder = os.path.dirname(sys.argv[0])
        if destination_folder:
            try:
                shutil.copy(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
                status_label.config(text="Đang chạy..")
                os.startfile(os.path.join(destination_folder, os.path.basename(file_path)))
                web_actions(os.path.join(destination_folder, os.path.basename(file_path)))
                root.destroy()
            except Exception as e:
                status_label.config(text="Lỗi: " + str(e))

        else:
            status_label.config(text="Không thể xác định!")

    else:
        status_label.config(text="Chưa chọn file excel!")


def web_actions(excel_file):
    path = r"C:\Users\kidfa\Desktop\Auto\chromedriver.exe" #123
    ser = Service(path)
    browser = webdriver.Chrome(service=ser)
    browser.get('https://chat.zalo.me/')
    browser.maximize_window()

    time.sleep(20)

    wb = xw.Book(excel_file)
    range = wb.sheets[0].range('C2:C21').value
    wb.close()

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
            message = input_message_entry.get()
            input = browser.find_element(By.XPATH, '//div[@id="input_line_0"]')
            input.click()
            input.send_keys(message)
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

    time.sleep(20)


def open_website(event):
    webbrowser.open_new("https://3b-artgallery.com/")

root = tk.Tk()
root.title("Automate Zalo")

input_message_label = tk.Label(root, text="Nhập tin nhắn:")
input_message_label.pack()
input_message_entry = tk.Entry(root, width=30)
input_message_entry.pack()

copy_button = tk.Button(root, text="Chọn file", command=copy_and_open_file)
copy_button.pack(pady=20)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

label = ttk.Label(root, text="Developed By Min Yoon © 2024")
label.pack(side=tk.BOTTOM, padx=5, pady=5)
label.bind("<Button-1>", open_website)

window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 3

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()