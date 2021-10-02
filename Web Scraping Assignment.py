# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:22:25 2021

@author: terry
"""

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver 
import time

url='https://us.burberry.com/womens-bags/'

browser=webdriver.Chrome('C:/Users/terry/Desktop/chromedriver.exe')
browser.get(url)

scroll=0

pageHeight=browser.execute_script('return document.documentElement.scrollHeight')

while scroll < pageHeight: 
    time.sleep(1)
    browser.execute_script('document.documentElement.scrollTop=' + str(scroll))
    scroll=scroll+200
    
pageObject= browser.execute_script('return document.body.innerHTML')

parsedObject= BeautifulSoup(pageObject,'html.parser')

bagContainers= parsedObject.find_all('div',class_='product-card__detail-wrapper product-listing-shelf__product-detail')

items_Data=pd.DataFrame(columns=['Bag Name','Bag Price'])

for items in bagContainers:
    try:
        items_name = items.find('p',class_='product-card__content-title').text
        items_price =items.find('span',class_='product-card__price-current').text
        new_items=pd.DataFrame(columns=['Bag Name','Bag Price'],data=[[items_name, items_price]])
        items_Data= items_Data.append(new_items)
    except:
        continue
