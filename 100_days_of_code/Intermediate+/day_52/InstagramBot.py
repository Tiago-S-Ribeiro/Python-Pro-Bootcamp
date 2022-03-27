from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import time
import os
load_dotenv()

#options = webdriver.ChromeOptions()
#options.add_argument("--incognito")
#https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de

SPEED_TEST_URL = os.getenv('SPEED_TEST_URL')
LOGIN_ID = os.getenv('LOGIN_ID')
TOKEN = os.getenv('TOKEN')
URL = os.getenv('URL')
TARGET_ACC = os.getenv('TARGET_ACC')
#----------------------------------------------------------------------------------------------------

class InstagramBot:

    def __init__(self, chromedriver_path_service):
        self.driver = webdriver.Chrome(service=Service(chromedriver_path_service))

    def login(self):
        #Get Instagram & accept cookies
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[2]").click()
        time.sleep(2)

        #Login with facebook
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Log in with Facebook')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[starts-with(@data-testid,'cookie-policy-manage-dialog-accept-button')]").click()
        time.sleep(2)
        email = self.driver.find_element(By.ID, "email")
        email.send_keys(LOGIN_ID)
        pwd = self.driver.find_element(By.ID, "pass")
        pwd.send_keys(TOKEN)
        self.driver.find_element(By.ID, "loginbutton").click()
        time.sleep(15)

        #Disable notifications
        try:
            self.driver.find_element(By.XPATH, "//button[starts-with(text(), 'Not Now')]")
        except NoSuchElementException:
            pass

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACC}/")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'followers')]").click()
        time.sleep(2)

    def follow(self):
        all_follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_follow_buttons:
            if button.text == "Follow":
                button.click()
                time.sleep(2)
            else:
                continue
