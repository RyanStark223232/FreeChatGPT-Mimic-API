# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:58:30 2023

@author: wongh
"""

import undetected_chromedriver as uc 
from selenium.webdriver.remote.webdriver import By
import re
import time 
import random

class ChatGPT_Mimic_API:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = uc.Chrome(use_subprocess=True, options=options)
        self.driver.set_window_size(800, 600)

    def _wait_between(self, min_value, max_value):
        random_float = random.uniform(min_value, max_value)
        time.sleep(random_float)

    def login(self):
        self.go_to()
        self.click_button("button[class='btn relative btn-primary']")
        self.fill_input(self.username, "username")
        self.click_button("button[class*='_button-login-id']")
        self.fill_input(self.password, "password")
        self.click_button("button[class*='_button-login-password']")
        self.click_button("button[class='btn relative btn-neutral ml-auto']")
        self.click_button("button[class='btn relative btn-neutral ml-auto']")
        self.click_button("button[class='btn relative btn-primary ml-auto']")
        return True

    def go_to(self, url = "https://chat.openai.com/"):
        time.sleep(0.5)
        self.driver.get(url)
        self._wait_between(0.5, 1)

    def click_button(self, css_selector = "button[class='btn relative btn-primary']"):
        button = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        button.click()
        self._wait_between(2, 2.5)

    def fill_textarea(self, text, css_selector = "textarea[placeholder='Send a message.']"):
        textarea = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        textarea.send_keys(text)
        self._wait_between(2, 2.5)

    def fill_input(self, text, element_id = "username"):
        input_element = self.driver.find_element(By.ID, element_id)
        input_element.clear()
        input_element.send_keys(text)
        self._wait_between(2, 2.5)
    
    def wait_for_generate(self,):
        count = 60
        self._wait_between(5, 10)
        last_response = self.get_response()
        while (count > 0):
            self._wait_between(2, 2.5)
            current_response = self.get_response()
            
            if current_response == last_response:
                break
            else:
                last_response = current_response
            count -= 1
        if count <= 0:
            raise Exception("Timeout: Generation took more than 5 minute.")
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
    with open("id_pass.txt", "r") as fp:
        splited = fp.read().split("\n")
        username, password = splited[0], splited[1]
    crawler = ChatGPT_Mimic_API(username, password)

    # Login Procedure
    crawler.login()

    # Example Input
    crawler.fill_textarea("Write something that sounds funny involving rick and ichigo", "textarea[placeholder='Send a message.']")
    crawler.click_button("button[class*='bottom']")
    crawler.wait_for_generate()
    response = crawler.get_response()
    print(f"***Generated Response {response}")
    
    crawler.exit_driver()