from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
##to opern webpage and print the title of the page

driver.get("https://www.youtube.com")

mytitle = driver.title()
print(mytitle)
driver.close(10)