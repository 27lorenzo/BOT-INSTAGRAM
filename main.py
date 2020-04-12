from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time 
import login
import getpages

driver = 0
username = "27reckless"
password = "lrnzbrrgr95"
max_likes = 10
max_follows = 10
refs = []
def main():
    global driver
    print("Running script")
    driver = webdriver.Chrome(r"C:\Users\loren\OneDrive\Documentos\CURSO PYTHON\BOT INSTAGRAM\chromedriver.exe")
    l = login.Login(driver, username, password)
    l.signin()
    time.sleep(3)
    gp = getpages.Getpages(driver)
    print(gp.get_number_followers())
    refs = gp.get_followers()
    run_bot(driver, refs, gp)


def run_bot(driver, refs, gp):
    print("LONGITUD: ", len(refs))
    print("accounts targeted")
    t = time.time()
    # how many pages we like/followed
    L = 0
    F = 0
    for r in refs:
        driver.get("https://www.instagram.com"+ r)
        time.sleep(1)
        if F < max_follows:
            try:
                print("current follows: " + str(F))
                gp.follow__public_page()
                print("ACCOUNT FOLLOWED")
                F += 1
                if L < max_likes:
                    gp.like_post()
                    L += 1
                    print("POST LIKED")
                else:
                    print("exceed the maximun number of likes")
                    break
            except:
                print("could not follow, private account")
                try:
                    gp.follow__private_page()
                    print("page followed succesfully")
                    F += 1
                except:
                    print("could not follow")    
        else:
            print("exceed the maximun number of follows")
            break
                    
if __name__== "__main__":
    main()