# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:38:27 2023

@author: m&m
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
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

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

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
#basically an exponetial growth model, we open all the feat chans of the first chan, then all for the 2nd gen, etc
#im not sure how ill visualise it but ill search graph theory python data science visualiser
