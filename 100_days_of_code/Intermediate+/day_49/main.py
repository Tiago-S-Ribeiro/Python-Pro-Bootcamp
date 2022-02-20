#browser.execute_script("window.history.go(-1)")   how to click 'back' on the browser
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
SIGN_IN_URL = os.getenv('SIGN_IN_URL')
LI_EMAIL = os.getenv('LI_EMAIL')
LI_PWD = os.getenv('LI_PWD')

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

role = input("Choose the desired role or software: ")
country = input("\nChoose the country/city: ")

service = Service(CHROMEDRIVER_PATH)
browser = webdriver.Chrome(service=service, options=options)
browser.get(SIGN_IN_URL)

#Accept Cookies
cookies = browser.find_element(By.XPATH, "//*[@id='artdeco-global-alert-container']/div/section/div/div[2]/button[2]")
time.sleep(1)
cookies.click()

#Sign In
username = browser.find_element(By.ID, "username")
username.send_keys(LI_EMAIL)
password = browser.find_element(By.ID, "password")
password.send_keys(LI_PWD)
time.sleep(2)
sign_in = browser.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
sign_in.click()
time.sleep(2)

#Find Jobs
jobs_tab = browser.find_element(By.LINK_TEXT, "Jobs")
jobs_tab.click()
time.sleep(2)

#Role
search_input = browser.find_element(By.XPATH, "//input[starts-with(@id,'jobs-search-box-keyword-id')]")
search_input.send_keys(role)
#Location
location_input = browser.find_element(By.XPATH, "//input[starts-with(@id,'jobs-search-box-location-id')]")
location_input.send_keys(country)

search_button = browser.find_element(By.XPATH, "//*[@id='global-nav-search']/div/div[2]/button[1]")
search_button.click()
time.sleep(2)

all_job_listings = browser.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in all_job_listings:
    job.click()
    time.sleep(1)

    try:
        company = browser.find_element(By.CSS_SELECTOR, ".jobs-unified-top-card__content--two-pane div span span a")
        print(company.text)

    except NoSuchElementException:
        print(">>This listing doesn't have a Company page.<<")
        continue

    except StaleElementReferenceException:
        all_job_listings = browser.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
        time.sleep(1.5)
        continue
