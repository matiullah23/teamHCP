# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:34:49 2021

@author: Austen
"""
# import dependencies
from bs4 import BeautifulSoup
import requests 
import pandas as pd 

##scraping skill ids and their descriptions
website = 'https://niccs.cisa.gov/workforce-development/cyber-security-workforce-framework/skills'

response = requests.get(website)

# check connection to website
response.status_code

# define soup variable
soup = BeautifulSoup(response.content, 'html.parser')
soup

# identify soup items
items = soup.find(id="edit-description").select('option[value]')
values = [item.get('value') for item in items]
textValues = [item.text.strip() for item in items]

 
print(values)
print(textValues)
    
len(values)
len(textValues)

##scraping task ids and their descriptions
website2 = 'https://niccs.cisa.gov/workforce-development/cyber-security-workforce-framework/tasks'

response2 = requests.get(website2)
response2.status_code

soup2 = BeautifulSoup(response2.content, 'html.parser')
soup2

items2 = soup2.find(id="edit-description").select('option[value]')
values2 = [item.get('value') for item in items2]
textValues2 = [item.text.strip() for item in items2]

 
print(values2)
print(textValues2)
    
len(values2)
len(textValues2)

##scraping knowledge ids and their descriptions

website3 = 'https://niccs.cisa.gov/workforce-development/cyber-security-workforce-framework/knowledge'

response3 = requests.get(website3)
response3.status_code

soup3 = BeautifulSoup(response3.content, 'html.parser')
soup3

items3 = soup3.find(id="edit-description").select('option[value]')
values3 = [item.get('value') for item in items3]
textValues3 = [item.text.strip() for item in items3]

 
print(values3)
print(textValues3)
    
len(values3)
len(textValues3)

##scraping ability ids and their descriptions

website4 = 'https://niccs.cisa.gov/workforce-development/cyber-security-workforce-framework/abilities'

response4 = requests.get(website4)
response4.status_code

soup4 = BeautifulSoup(response4.content, 'html.parser')
soup4

items4 = soup4.find(id="edit-description").select('option[value]')
values4 = [item.get('value') for item in items4]
textValues4 = [item.text.strip() for item in items4]

 
print(values4)
print(textValues4)
    
len(values4)
len(textValues4)

##Creating a dataframe for the KSA id's and their descriptions
NIST_NICE_Reference_Data = pd.DataFrame({'ID' : values + values2 + values3 + values4, 'Description': textValues + textValues2 + textValues3 + textValues4})
NIST_NICE_Reference_Data = NIST_NICE_Reference_Data.drop([0])
NIST_NICE_Reference_Data

##Converting the dataframe to an excel file
NIST_NICE_Reference_Data.to_excel('NIST_NICE_Reference_Data.xlsx', index=False)
