from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UsedCar:
    def __init__(self, make, model, miles, price, platform_link):
        self._make = make
        self._model = model
        self._miles = miles
        self._price = price
        self._platform_link = platform_link

    def display_info(self):
        print(f"Make: {self._make}")
        print(f"Model: {self._model}")
        print(f"Miles: {self._miles}")
        print(f"Price: {self._price}")
        print(f"Platform Link: {self._platform_link}")

    # Setter methods
    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_miles(self, miles):
        self._miles = miles

    def set_price(self, price):
        self._price = price

    def set_platform_link(self, platform_link):
        self._platform_link = platform_link



PATH = "C:/Program Files (x86)/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.goauto.ca/vehicles?refinementList=%7B%22stock_type%22%3A%5B%22USED%22%5D%2C%22make_name%22%3A%5B%22Acura%22%5D%7D")

#print(driver.title)
#print(driver.page_source)
try:
    text_box = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_inventoryListing__vHmrR"))
    )
    time.sleep(30)
    links = text_box.find_elements(By.CLASS_NAME, 'inventory_imageWrapper__xHDnp')
    for link in links:
       link_to_there = link.get_attribute('href')
       print(link_to_there)
       element_to_image = link.find_element(By.TAG_NAME, 'img')
       link_to_image = element_to_image.get_attribute('src')
       print(link_to_image)

except:
    driver.quit()






