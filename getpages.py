from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time 


class Getpages:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get("https://www.instagram.com/python.learning/")
        self.hrefs = []

    def get_number_followers(self):
        flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main")))
        soup_flw = b(flw.get_attribute("innerHTML"), "html.parser") #We get all the code html
        flw_class = soup_flw.findAll("span", {"class": "g47SY"}) #select class g47SY from the whole code
        flw_num = flw_class[1].getText() #[0]: number of posts, [1]: number of followers, [2]: number of followings
        if "k" in flw_num:
            flw_num = float(flw_num[:-1])*10**3
            return flw_num
        elif "m" in flw_num:
            flw_num = float(flw_num[:-1])*10**flw_num
            return flw_num
        else:
            return float(flw_num)

    def get_followers(self):
        time.sleep(2)
        flw_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span")))
        flw_button.click()
        time.sleep(3)
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]")))
        for h in range(11):
            time.sleep(1)
            print("arguments[0].scrollTop = arguments[0].scrollHeight/{}".format(str(11-h)))
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/{}".format(str(11-h)), self.popup)
            if h == 5:
                break
        
        #We made scroll in the scrollbar 40 times
        for i in range(40):
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.popup)
        
        self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]")))
        b_popup = b(self.popup.get_attribute("innerHTML"), "html.parser")
        for p in b_popup.findAll("li", {"class": "wo9IH"}): #wo9IH: common class of each follower
            try:
                hlink = p.find_all("a")[0]["href"] #get the username from each user
                print(hlink)
                if "div" in hlink:
                    print("div found not adding to list")
                else:
                    self.hrefs.append(hlink)
            except:
                pass
        return self.hrefs

    def is_public(self): # I don't use this function
        try:
            state = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"rkEop")))
            if state.text == "Esta cuenta es privada":
                return False
            else:
                return True
        except:
            return True # it will return True in case the account is public
    
    def like_post(self):
        post = self.driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1)")
        h = b(post.get_attribute("innerHTML"), "html.parser")
        href = h.a["href"] #We get the specific url of each post
        self.driver.get("https://www.instagram.com" + href)
        like_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")))
        like_button.click()

    def follow__public_page(self):
        follow = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button")))
        f_text = follow.text
        if f_text.lower() == "seguir" or f_text.lower() == "seguir también":
            follow.click()
        elif f_text.lower() == "siguiendo":
            print("Ya siguiendo")
        time.sleep(2)
    
    def follow__private_page(self):
        follow = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main > div > header > section > div.nZSzR > button")))
        f_text = follow.text
        if f_text.lower() == "seguir" or f_text.lower() == "seguir también":
            follow.click()
        elif f_text.lower() == "siguiendo":
            print("Ya siguiendo")
        time.sleep(2)
        