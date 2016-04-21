import requests
import sys
import bs4
from bs4 import BeautifulSoup
import pandas as pd


#Configuration parameters
url_dummy = 'https://nfg.sefaz.rs.gov.br/Login/LoginNfbsdsasax'
login_url = 'https://nfg.sefaz.rs.gov.br/Login/LoginNfg.aspx'
headers = {'user-agent': 'my-app/0.0.1'}
user='95511709034'
passwd='123dealmeida4' 

def trade_spider():
	url='http://www.stratoslab.io/#ribbon'
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	for link in soup.findAll('a',{'class':'itemhead'}):
		href=link.get('href')
		print(href)

# main
trade_spider(2)	