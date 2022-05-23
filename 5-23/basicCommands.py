from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.youtube.com/")
print(driver.title)

driver.get("https://www.facebook.com/")

driver.back()

driver.forward(5)