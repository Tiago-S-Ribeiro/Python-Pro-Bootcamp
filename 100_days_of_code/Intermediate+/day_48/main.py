from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import time
import os

os.system("clear")
load_dotenv()
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
FIVE_MINS = time.time() + 60 * 5

service = Service(CHROMEDRIVER_PATH)
browser = webdriver.Chrome(service=service)
browser.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = browser.find_element(By.ID, "cookie")

def purchase():
    money = int(browser.find_element(By.ID, "money").text.replace(",",""))
    
    store = browser.find_elements(By.CSS_SELECTOR, "#store div b ")[:-1]
    store_prices = [int(item.text.split("-")[1].strip().replace(",","")) for item in store]

    try:
        for price in store_prices[::-1]:
            if money >= price:
                store[store_prices.index(price)].click()
                break
    except StaleElementReferenceException:
        store = browser.find_elements(By.CSS_SELECTOR, "#store div b")[:-1]
        store_prices = [int(item.text.split("-")[1].strip().replace(",","")) for item in store]


timeout = time.time() + 5 

while time.time() < FIVE_MINS:
    cookie.click()
    
    if time.time() > timeout:
        purchase()
        timeout = time.time() + 5

print(browser.find_element(By.ID, "cps").text)

browser.close()
browser.quit()