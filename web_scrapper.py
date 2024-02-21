from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
import time
from pynput import keyboard

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

Link = "https://orteil.dashnet.org/cookieclicker/"
driver.get(Link)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]'))
)

language_element = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language_element.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'bigCookie'))
)

cookie_element = driver.find_element(By.ID, 'bigCookie')
cookie_element.click()

time.sleep(30)

driver.quit()
