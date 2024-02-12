from selenium import webdriver
from instagramUserInfo import username,password
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Controller, Button
import tkinter as tk
import keyboard
import numpy as np
import random
import time

class Instagram:
    def __init__(self,username,password):
        self.__random_sleep
        self.__makeScroll
        self.__makeCenter
        self.__tiklama
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password 
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        emailInput = self.browser.find_element(By.CSS_SELECTOR,value="#loginForm > div > div:nth-child(1) > div > label > input")
        passwordInput = self.browser.find_element(By.CSS_SELECTOR,value="#loginForm > div > div:nth-child(2) > div > label > input")
        emailInput.send_keys(self.username)
        time.sleep(2)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
    
    def __random_sleep(self,min_sleep_time, max_sleep_time):
            sleep_time = random.uniform(min_sleep_time, max_sleep_time)
            time.sleep(sleep_time)

    
    def __tiklama(self):
            keyboard.press('tab')
            time.sleep(5)
            keyboard.press('tab')  
            time.sleep(5)    
            keyboard.press('enter')
            
    def __makeCenter(self):
        mouse = Controller()
        screen_width = tk.Tk().winfo_screenwidth()
        screen_height = tk.Tk().winfo_screenheight()
        mouse.position = (screen_width / 2, screen_height / 2)
        
    def __makeScroll(self):
        mouse = Controller()
        scroll_direction = 'down' 
        scroll_amount = 120
        if scroll_direction == 'up':
            mouse.scroll(0, scroll_amount)
        elif scroll_direction == 'down':
            mouse.scroll(0, -scroll_amount)
            
    def getFollowers(self):
        self.__random_sleep(4,8)
        self.browser.get(f"https://www.instagram.com/{self.username}/following/")
        time.sleep(10)
        self.browser.maximize_window()
        time.sleep(10)
        self.__makeCenter()
        time.sleep(10)
        self.__makeScroll()
        time.sleep(10)
        followings = self.browser.find_elements(By.CSS_SELECTOR,value="div[role=dialog] button")
        count = 1
        for button in followings:
            if(count == 1):
                count +=1
                continue
            time.sleep(5)
            button.click()
            time.sleep(5)
            self.__tiklama()
        time.sleep(100)
    
instgrm = Instagram(username,password)   
instgrm.signIn()
instgrm.getFollowers()