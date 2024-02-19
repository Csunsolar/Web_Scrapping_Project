from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
import time

Link = "https://quotes.toscrape.com/"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(Link)



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col-md-4"))
    )
finally:
    input_element = driver.find_element(By.CLASS_NAME, "col-md-4").click() #this is for input


time.sleep(10)

driver.quit()