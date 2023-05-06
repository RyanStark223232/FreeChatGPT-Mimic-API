# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:58:30 2023

@author: wongh
"""

import undetected_chromedriver as uc 
from selenium.webdriver.remote.webdriver import By
import re
import time 

class ChatGPT_Mimic_API:
    def __init__(self):
        options = uc.ChromeOptions()
        self.driver = uc.Chrome(use_subprocess=True, options=options)

    def go_to(self, url = "https://chat.openai.com/"):
        time.sleep(0.5)
        self.driver.get(url)
        input("Please Input All Necessary Information Until You See the Textarea, Then Press Enter in the Command Prompt")

    def enter_text(self, text, css_selector = "textarea[placeholder='Send a message.']"):
        textarea = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        textarea.send_keys(text)
        time.sleep(0.5)

    def click_send(self, css_selector = "button[class*='bottom']"):
        button = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        button.click()
        time.sleep(0.5)
    
    def wait_for_generate(self,):
        count = 12
        time.sleep(5)
        last_response = self.get_response()
        while (count > 0):
            time.sleep(5)
            current_response = self.get_response()
            
            if current_response == last_response:
                break
            else:
                last_response = current_response
            count -= 1
        if count <= 0:
            raise Exception("Timeout: Generation took more than 1 minute.")
        return True
    
    def get_response(self, index = -1):
        response_divs = self.driver.execute_script(
            "return document.querySelectorAll('main > div > div > div > div > div > div > div > div > div > div[class*=markdown]');"
        )
        if len(response_divs) == 0: return False
        return response_divs[index].text
        
    def new_chat(self, url = "https://chat.openai.com/"):
        self.driver.get(url)
        time.sleep(1)
        if not self.get_response(): 
            return True
        else:
            return self.new_chat()
        
    def exit_driver(self):
        self.driver.quit()
        
if __name__ == "__main__":
    crawler = ChatGPT_Mimic_API()
    urls = crawler.go_to()
    crawler.enter_text("Write a 2 lines resume.")
    crawler.click_send()
    crawler.wait_for_generate()
    response = crawler.get_response()
    print(response)
    input()
    crawler.exit_driver()