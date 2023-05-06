# -*- coding: utf-8 -*-
"""
Created on Sat May  6 17:11:20 2023

@author: wongh
"""

import undetected_chromedriver as uc 
from selenium.webdriver.remote.webdriver import By
from bs4 import BeautifulSoup
import re
import time 

options = uc.ChromeOptions()
driver = uc.Chrome(use_subprocess=True, options=options)

driver.get("https://chat.openai.com/")

textarea = driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Send a message.']")
textarea.send_keys("Draw a potato in ASCII")

button = driver.find_element(By.CSS_SELECTOR, "button[class*='bottom']")
button.click()

button = driver.find_element(By.CSS_SELECTOR, "button[class*='btn relative btn-neutral border-0 md:border']")
button.click()

response_divs = driver.execute_script("return document.querySelectorAll('main > div > div > div > div > div > div > div > div > div > div[class*=markdown]');")
print(response_divs[-1].text)
