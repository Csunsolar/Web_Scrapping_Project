from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options

PATH = r"C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions() 
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(
    service= Service(PATH), 
    options=options)

driver.get("https://quotes.toscrape.com/")
print(driver.title)
driver.quit()