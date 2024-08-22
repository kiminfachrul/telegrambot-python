import schedule
import time
import pyautogui
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import webbrowser

user_data = "user-data-dir=C:\\Users\\Faul Islam\\AppData\\Local\\Google\\Chrome\\User Data\\Default" #Bisa di koment saja
    
# URL Spreadsheet yang ditargetkan
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1e1wzZ1tSgQmsp7wEFon5QC-l9pu26s0PE7vkvEOMsiU/edit?hl=id&gid=909500613#gid=909500613"  # Ganti dengan URL spreadsheet yang diinginkan

def open_chrome_and_screenshot(save_path):
    # Buka Chrome dan arahkan ke URL Spreadsheet
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' #Bisa cek di browser lalu cari chrome://version/
      # Path ke aplikasi Chrome
    webbrowser.get(chrome_path).open(SPREADSHEET_URL)

    # Beri waktu untuk Chrome memuat halaman
    time.sleep(10)  # Sesuaikan waktu ini jika halaman membutuhkan waktu lebih lama untuk memuat
    
    # Mengambil screenshot seluruh layar
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)
    print(f"Screenshot saved to {save_path}")
    pyautogui.hotkey('alt', 'f4')

def schedule_screenshot(save_path, schedule_time):
    # Penjadwalan screenshot sesuai jadwal yang diinginkan
    schedule.every().day.at(schedule_time).do(open_chrome_and_screenshot, save_path=save_path)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
