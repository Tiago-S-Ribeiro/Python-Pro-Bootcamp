#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import os

os.system("clear")
load_dotenv()

CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

service = Service(CHROMEDRIVER_PATH)
browser = webdriver.Chrome(service=service)
browser.get('https://www.python.org/')

events_list = browser.find_elements_by_css_selector('div.medium-widget.event-widget.last ul li')
events = {}

for i in range(len(events_list)):
    events[i] = {"time": events_list[i].text.splitlines()[0], "name": events_list[i].text.splitlines()[1]}

print(events)

browser.quit()