from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import time
import os

os.system("clear")
load_dotenv()

CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
URL = os.getenv('URL')
EMAIL = os.getenv('EMAIL')
FB_PWD = os.getenv('FB_PWD')
P_NUM = os.getenv('P_NUM')

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

service = Service(CHROMEDRIVER_PATH)
browser = webdriver.Chrome(service=service, options=options)
browser.get(URL)

#Accept Tinder's Cookies
time.sleep(0.5)
cookie = browser.find_element(By.XPATH, "//button[starts-with(@data-testid,'privacyPreferencesAccept')]")
time.sleep(2)
cookie.click()

login = browser.find_element(By.XPATH, "//*[contains(text(), 'Log in')]")
login.click()
time.sleep(2)

facebook = browser.find_element(By.XPATH, "//button[starts-with(@data-testid,'login')]")
facebook.click()
time.sleep(2)

#Change focus to the popup page
base_page = browser.window_handles[0]
facebook_popup_page = browser.window_handles[1]
browser.switch_to.window(facebook_popup_page)

#Accept Facebook's Cookies
fb_cookies = browser.find_element(By.XPATH, "//button[starts-with(@data-testid,'cookie-policy-manage-dialog-accept-button')]")
fb_cookies.click()
time.sleep(2)

#Login w/ Facebook
email = browser.find_element(By.ID, "email")
email.send_keys(EMAIL)
password = browser.find_element(By.ID, "pass")
password.send_keys(FB_PWD.strip())

fb_login = browser.find_element(By.XPATH, "//input[starts-with(@value,'Log In')]")
fb_login.click()
time.sleep(2)

fb_continue = browser.find_element(By.XPATH, "//*[contains(text(), 'Jeremiah')]")
fb_continue.click()
time.sleep(3)

#Insert Phone Number
browser.switch_to.window(base_page)
phone_num = browser.find_element(By.XPATH, "//input[starts-with(@data-testid,'phoneNumberInput')]")
phone_num.send_keys(P_NUM)

for i in range(100):
    like_button = browser.find_element_by_xpath("//*[contains(text(), 'Nope')]")
    like_button.click()