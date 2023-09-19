# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:38:27 2023

@author: m&m
"""

#selenium learning (for youtube spider and chatgptree)
from selenium import webdriver
#from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def scroll_to_bottom(scroll_distance = 500, pause = 2): #Made by chatgpt
    initial_scroll_position = driver.execute_script("return window.scrollY;")
    while True:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(pause)
        current_scroll_position = driver.execute_script("return window.scrollY;")
        if current_scroll_position == initial_scroll_position:
                break
        initial_scroll_position = current_scroll_position

def click_arrows():
    try:
        for i in range(1,3):
            arrow = driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[{i}]/div[3]/ytd-shelf-renderer/div[1]/div[2]/yt-horizontal-list-renderer/div[3]/ytd-button-renderer')
            arrow.click()
            time.sleep(1)
    except:
        ""

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')  # Enable headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU to avoid some issues

driver = webdriver.Chrome(chrome_options)
driver.get('https://www.youtube.com/@AdamRyman/channels')
driver.implicitly_wait(3)

try:
    scroll_to_bottom(600,.5)
    click_arrows()
    channels1 = driver.find_elements(By.TAG_NAME, 'ytd-grid-channel-renderer')
    name_li = []
    for channel in channels1:
        name = channel.find_element(By.ID, 'title').get_attribute('innerHTML')
        if name not in name_li:
            name_li.append(name)
        link = channel.find_element(By.ID, 'channel-info').get_attribute('href')
    print(name_li)
finally:
    driver.quit()

#here is where the recursion would go
	#either click or get the link and open the url for the first featured channel
	#featured_channels1.1.1 loop etc
#def open_channels():
#	open_channels()


#to save the channels, ill save the channel name and how many times they were reffered to, so either a dictionary or a list with each element as a touple/list[2]
#channels = {"Name"=num,...} or [("Name", num),...] or [["Name", num],...]
#wait till i can find the featured channels
#featured_channels1 = [...] #I could have a data structure that holds the hole chart/graph, idk how but im thinking a list where each element (channel) becomes a list containing the channels in it.



#I think i can use recursion to go through all the channels
#I am going to go channel by channel, instead of 1st channel till end (maybe no end, maybe loop)
#basically an exponetial growth model, we open all the feat chans of the first chan, then all for the 2nd gen, etc
#im not sure how ill visualise it but ill search graph theory python data science visualiser