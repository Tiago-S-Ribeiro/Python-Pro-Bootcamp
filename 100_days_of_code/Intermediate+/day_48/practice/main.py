#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import os

os.system("clear")
load_dotenv()

PRODUCT_URL = os.getenv('PRODUCT_URL')
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

# 1
# chrome_driver_path = "/Users/tiago.soaresribeiro/Documents/Personal_Docs/tiago_documents/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get('https://www.amazon.com')

# 2
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get('https://www.amazon.com')
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python

# 3
#service = Service(CHROMEDRIVER_PATH)
#browser = webdriver.Chrome(service=service)
#browser.get(PRODUCT_URL)

#price = browser.find_element(by="id", value="price")
#test = browser.find_element_by_xpath('//*[@id="histogramTable"]/tbody/tr[1]/td[3]/span[2]/a')
#print(test.text)


service = Service(CHROMEDRIVER_PATH)
browser = webdriver.Chrome(service=service)
browser.get('https://www.python.org/')

events_list = browser.find_elements_by_css_selector('div.medium-widget.event-widget.last ul li')
events = {}
#print(events_list[0].find_element(By.CSS_SELECTOR, 'time').text)

for i in range(len(events_list)):
    events[i] = {"time": events_list[i].text.splitlines()[0], "name": events_list[i].text.splitlines()[1]}

print(events)

browser.close()
browser.quit()