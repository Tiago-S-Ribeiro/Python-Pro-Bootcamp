from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from dotenv import load_dotenv
import os

os.system("clear")
load_dotenv()

CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

service = Service(CHROMEDRIVER_PATH)
browser = webdriver.Chrome(service=service)
browser.get('https://en.wikipedia.org/wiki/Main_Page')

count = browser.find_element(By.CSS_SELECTOR, "#articlecount a")
#count.click()

all_portals = browser.find_element(By.LINK_TEXT, "All portals")
#all_portals.click()

search_bar = browser.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
