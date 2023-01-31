from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



username=['student','student','nishan','srijana','pratham']
password=['Password123','hello','yellow','carrot','computer']


def simpleTest(username,password):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='username']").send_keys(username)
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
    time.sleep(2)
    driver.find_element(By.ID,'submit').click();
    time.sleep(2)
    if driver.current_url=='https://practicetestautomation.com/logged-in-successfully/':
        print("Login Success")
    else:
        print("Login Not Sucess")

for x in range(5):
    simpleTest(username[x],password[x])
    time.sleep(2) #waits 5 sec for next iterations
    
    
