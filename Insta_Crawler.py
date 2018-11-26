# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Safari()
        
        
    def closeBrowser(self):
        self.driver.close()
        
    def login(self):
         driver = self.driver
         driver.get("https://www.instagram.com")
         time.sleep(2)
         login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
         login_button.click()
         time.sleep(2)
         user_name_elem = driver.find_element_by_xpath('//*[@name="username"]')
         user_name_elem.clear()
         user_name_elem.send_keys(self.username)
         password_elem = driver.find_element_by_xpath('//*[@name="password"]')
         password_elem.clear()
         password_elem.send_keys(self.password)
         password_elem.send_keys(Keys.RETURN)
         time.sleep(5)
         notifications_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]')
         notifications_button.click()
         
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(2)
        for i in range(1 , 4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        #searching for picture link
        
        hrefs = driver.find_elements_by_tag_name('a')
        pichrefs = [elem.get_attribute("href") for elem in hrefs]
        pichrefs = [href for href in pichrefs]
        
        for pichref in pichrefs:
            driver.get(pichrefs)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_link_text("Like").click()
                time.sleep(18)
            except Exception as e:
                time.sleep(2)
        
        
         
password = "Password"
username = "username"     
juansBot = InstagramBot(password, username)
juansBot.login()
juansBot.like_photo("newyork")
juansBot.closeBrowser()