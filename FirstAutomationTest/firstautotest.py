from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#webdriver-manager  3.5.4 package for online browser driver import
#from selenium import webdriver;
#driver=webdriver.Chrome(executable_path="C:\BrowserDriver\chromedriver.exe");

username=['student','student','nishan','srijana','pratham']
password=['Password123','hello','yellow','carrot','computer']


def simpleTest(username,password):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    driver.find_element_by_id('submit').click();
    if driver.current_url=='https://practicetestautomation.com/logged-in-successfully/':
        print("Login Success")
    else:
        print("Login Not Sucess")

for x in range(5):
    simpleTest(username[x],password[x])
    
    
