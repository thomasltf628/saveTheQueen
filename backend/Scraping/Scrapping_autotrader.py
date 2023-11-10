import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

url = "https://www.autotrader.ca/cars/?rcp=0&rcs=0&prx=100&hprc=True&wcp=True&sts=New-Used&inMarket=basicSearch&mdl=A6&make=Audi&loc=L1G0C5"
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'}
response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.content, 'html.parser') 
print(response.status_code) 