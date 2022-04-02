from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import time
import os

load_dotenv()

LOGIN_ID = os.getenv('LOGIN_ID')
TOKEN = os.getenv('TOKEN')
FORM = os.getenv('FORM')

class FormFillerBot:

    def __init__(self, chromedriver_path_service):
        self.driver = webdriver.Chrome(service=Service(chromedriver_path_service))

    def fill_google_form(self, listings):
        for item in listings:
            self.driver.get(FORM)
            time.sleep(1)
            self.driver.find_element(By.ID, "identifierId").send_keys(LOGIN_ID)
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'Seguinte')]")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys(TOKEN)
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'Seguinte')]")
            time.sleep(30)

            if item['house'] == "Apartamento":
                self.driver.find_element(By.XPATH, "//*[contains(text(), 'Apartamento')]").click()
            else:
                self.driver.find_element(By.XPATH, "//*[contains(text(), 'Moradia')]").click()
            
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(item['region'])
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(item['price'])
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(item['description'])
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(item['realtor'])
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(item['link'])
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
            time.sleep(5)