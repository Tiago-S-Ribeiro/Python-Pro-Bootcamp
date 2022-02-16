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
browser.get('http://secure-retreat-92358.herokuapp.com/')

first_name = browser.find_element(By.NAME, "fName")
first_name.click()
first_name.send_keys("Tiago")

last_name = browser.find_element(By.NAME, "lName")
last_name.click()
last_name.send_keys("Ribeiro")

email_adr = browser.find_element(By.NAME, "email")
email_adr.click()
email_adr.send_keys("tiago.ribeiro@email.com")

button = browser.find_element(By.CSS_SELECTOR, "form.form-signin button")
button.click()