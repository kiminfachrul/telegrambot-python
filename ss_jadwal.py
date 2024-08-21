from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from telegram import Bot

# Path configuration
CHROME_DRIVER_PATH = 'D:\chromedriver-win64\chromedriver.exe'  # Update this to your chromedriver path
CHROME_EXECUTABLE_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
PROFILE_PATH = 'C:\\Users\\Fachrul Islam\\AppData\\Local\\Google\\Chrome\\User Data\\Default'

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={PROFILE_PATH}")
chrome_options.binary_location = CHROME_EXECUTABLE_PATH

# Function to take a screenshot
def take_screenshot(chat_id):
    url = 'https://docs.google.com/spreadsheets/d/1e1wzZ1tSgQmsp7wEFon5QC-l9pu26s0PE7vkvEOMsiU/edit?gid=909500613#gid=909500613'  # Update this to your spreadsheet link
    screenshot_path = f'screenshot_{int(time.time())}.png'

    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Take screenshot
        driver.save_screenshot(screenshot_path)

        # Send the screenshot via Telegram
        send_screenshot(chat_id, screenshot_path)
    finally:
        driver.quit()

    # Clean up
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

def send_screenshot(chat_id, screenshot_path):
    # Initialize bot
    bot = Bot(token='7473429203:AAH_SA2JlEtIZZfQ9m7ysh0bLgAsduy1exo')

    try:
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
    except Exception as e:
        print(f"Error sending screenshot: {e}")