from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import time
import os
load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

SPEED_TEST_URL = os.getenv('SPEED_TEST_URL')
LOGIN_ID = os.getenv('LOGIN_ID')
TOKEN = os.getenv('TOKEN')
URL = os.getenv('URL')
#----------------------------------------------------------------------------------------------------

class InternetSpeedTwitterBot:
    
    def __init__(self, chromedriver_path_service):
        self.driver = webdriver.Chrome(service=Service(chromedriver_path_service), options=options)
        self.upload = 0
        self.download = 0
    
    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        cookies = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        cookies.click()
        time.sleep(1)

        test = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        test.click()
        time.sleep(45)

        try:
            close_ad = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a")
            close_ad.click()
            time.sleep(1)
        except Exception:
            pass

        self.download = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        self.upload = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text

    def tweet_at_provider(self):
        self.driver.get(URL)
        time.sleep(5)

        phone_num = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        phone_num.send_keys(LOGIN_ID)

        next = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span")
        next.click()
        time.sleep(5)

        password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TOKEN)
        time.sleep(1)

        login = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Log in')]")
        login.click()
        time.sleep(3)

        cookies = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div[2]/div[1]/div/span/span")
        cookies.click()
        time.sleep(1)

        input_box = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        input_box.click()
        input_box.send_keys(f"Hey @VodafonePT, why's my internet speed {self.download} DOWN / {self.upload} UP when I pay for 500 DOWN / 100 UP ??")

        tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet.click()
        time.sleep(2)

        check_profile = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div/div")
        check_profile.click()
        