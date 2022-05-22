from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

username = 'student'
password = 'Password123'

def SingupLogoutTest(username,password):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@id='submit']").click()
    driver.find_element_by_xpath("//a[normalize-space()='Log out']").click()
    
SingupLogoutTest(username,password)
    