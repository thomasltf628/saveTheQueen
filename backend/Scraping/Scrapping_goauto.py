import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

def get_data():
    url = 'https://www.goauto.ca/vehicles?refinementList=%7B%22stock_type%22%3A%5B%22NEW%22%5D%2C%22make_name%22%3A%5B%22Ford%22%5D%2C%22model_name%22%3A%5B%22F-150%22%5D%7D'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(r.status_code)
    return soup

get_data()
