import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

def get_data():
    url = 'https://www.kijijiautos.ca/cars/ford/bronco/used/#con=USED&ms=9000%3B3&od=down&sb=rel'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(r.status_code)
    return soup

get_data()
