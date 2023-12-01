#This script require multiple scrapping, as only 21 record could be scrappedeach time
#loop over different make and model at a time interval
#choose place

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import datetime
from Model_and_Make_list import make_and_model_list
import re
from selenium.webdriver.common.keys import Keys



make_list = make_and_model_list()[0]
model_list = make_and_model_list()[1]
years = []
curr_year = int((str(datetime.date.today()))[:4])
for i in range (curr_year - 20, curr_year+1):
    years.append(i)
for index, year in enumerate(years):
    year = str(year)
    years[index] = year

url = "https://www.kijijiautos.ca/cars/#od=down&sb=rel"
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'}
PATH = "C:/Program Files (x86)/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

def extract_car_info(car_info):
    
    make_pattern = re.compile(r'\b(?:' + '|'.join(make_list) +r')\b', flags=re.IGNORECASE)
    model_pattern = re.compile(r'\b(?:' + '|'.join(model_list) +r')\b', flags=re.IGNORECASE)
    year_pattern = re.compile(r'\b(?:' + '|'.join(years) +r')\b', flags=re.IGNORECASE)
    

    make_match = make_pattern.search(car_info)
    model_match = model_pattern.search(car_info)
    year_match = year_pattern.search(car_info)

    make = make_match.group() if make_match else None
    model = model_match.group() if model_match else None
    year = year_match.group() if year_match else None

    return make, model, year

driver.get(url)
page_num = 2
max_failures = 5
failures = 0
page_to_scrap = 2
scrap_fail = 0
num_of_count_remains = 10
website = 'kijijiauto'
locarion_of_searcher = 'Toro'
data ={
        'Source':[],
        'Make':[],
        'Model':[],
        'year':[],
        'price':[],
        'mileage':[],
        'location':[],
        'listing_date':[],
        'link_to_buyer':[],
        'link_to_image':[],
    }
df = pd.DataFrame(data)

try:

    button_element = driver.find_element(By.CSS_SELECTOR, '[data-testid="LocationLabelLink"]')
    print('found button')

    driver.execute_script("arguments[0].click();", button_element)
    print('clicked button')

    input_area = WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.ID, 'LocationAutosuggest'))
            )
    input_area.send_keys(locarion_of_searcher)
    time.sleep(2)
    input_area.send_keys(Keys.BACKSPACE * 1)
    time.sleep(10)
    print('entered toronto')
    time.sleep(5)
    submit_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="LocationModalSubmitButton"]')
    driver.execute_script("arguments[0].click();", submit_button)
    print('clicked')

except:
    print('location already settled')

try:
    text_box = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="SearchResultList"]'))
        )
    print('good')
    time.sleep(3)
    blocks = text_box.find_elements(By.TAG_NAME, 'article')
    print('goodgood')
    for block in blocks:
        num_of_count_remains -= 1
        try:
            id_car = block.find_element(By.CSS_SELECTOR, '[data-testid="VehicleListItem"]').get_attribute('data-test-ad-id')
            print(id_car)
            link_to_buyer = f'https://www.kijijiautos.ca/vip/{id_car}'
            year_make_and_model =  block.find_element(By.TAG_NAME, 'h2')
            make, model, year = extract_car_info(year_make_and_model.text)
            print(make,model,year)
            price = block.find_element(By.CLASS_NAME, 'mcN7dZ').find_element(By.CSS_SELECTOR, '[data-testid="searchResultItemPrice"]')
            price_todf = price.text
            for char in '$,"':
                price_todf = price_todf.replace(char, '')
            print(price_todf)
            mileage_location = block.find_element(By.CLASS_NAME, 'icN7dZ').find_elements(By.TAG_NAME, 'li')
            for index, ele in enumerate (mileage_location):
                dummy = ele.find_element(By.TAG_NAME, 'span')
                if index == 0:
                    mileage = dummy.text
                    for char in 'km, "':
                        mileage = mileage.replace(char, '')
                    print(mileage)
                elif index == 1:
                    location = dummy.text
                    print(location)
                else:
                    continue
                            
            listing_date = datetime.date.today()            
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'b1E1YI')))
            img_element = element.find_element(By.TAG_NAME, 'img')
            link_to_image = img_element.get_attribute('src')
            print(link_to_image)
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)
            df.loc[len(df.index)] = [website, make, model, year, price_todf, mileage, location,listing_date,link_to_buyer,link_to_image]
        except:
            scrap_fail += 1
            print (f'{scrap_fail} piece of information fails to be scrapped')
            continue
        if num_of_count_remains == 0:
            df.to_csv(f'{website}.csv', index=False)  
            driver.quit()
            break
        time.sleep(0.5)
except Exception as e:
    print(f'Exception: {str(e)}')
    failures += 1
    if failures >= max_failures:
        df.to_csv(f'{website}.csv', index=False)
        print(f'Maximum failures ({max_failures}) reached. Exiting...')
        driver.quit()
df.to_csv(f'{website}.csv', index=False)  
