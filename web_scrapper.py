from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
cookie_click_ID = "bigCookie"
cookies_ID = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"


Link = "https://orteil.dashnet.org/cookieclicker/"
driver.get(Link)

#waits for element to load on browser and then continues
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]'))
)

language_element = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language_element.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_click_ID))
)

cookie_element = driver.find_element(By.ID, cookie_click_ID)

while True:
    cookie_element.click()
    number_of_cookies = driver.find_element(By.ID, cookies_ID).text.split(" ")[0]
    number_of_cookies = int(number_of_cookies.replace(",",""))

#four products to buy. This for loop will check each item to see if it is purchasable
    for y in range(4): 
        product_price = driver.find_element(By.ID, product_price_prefix + str(y)).text.replace(",", "") 

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

#purchases product that can be afforded
        if number_of_cookies >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(y))
            product.click()
            break