from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
from selenium.webdriver.common.keys import Keys
import time

class Login:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password
    def signin(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        #WebDriverWait: it will waits 5 seconds before giving up if it doens't find the username css selector
        ID = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")))
        ID.click()
        ID.send_keys(self.username)
        passw = self.driver.find_element_by_xpath("//input[@name='password']")
        passw.click()
        passw.send_keys(self.password)
        passw.send_keys(Keys.ENTER)
        #button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/button")
        #button.click()
        #time.sleep(10)
        #<input aria-label="Contraseña" aria-required="true" autocapitalize="off" autocorrect="off" name="password" type="password" class="_2hvTZ pexuQ zyHYP" value="">