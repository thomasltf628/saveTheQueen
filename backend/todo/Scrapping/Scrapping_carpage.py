import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

url = "https://www.carpages.ca/used-cars/search/?make_name=toyota&model_name=camry"
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'}
response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.content, 'html.parser') 
print(response.status_code) 