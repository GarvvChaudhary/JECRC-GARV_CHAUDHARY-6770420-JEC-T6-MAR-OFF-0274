import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(3)

#to the botton of the page
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(2)

#to the origin of the page
driver.execute_script('window.scrollTo(0,0);')
sleep(2)

#using Scroll By
driver.execute_script('window.scrollBy(0,500);') #scrolling down to 500px
sleep(2)
driver.execute_script('window.scrollBy(0,-300);') #scrolling up 300px from 500px
sleep(2)

#scrolling to element
element = driver.find_element(By.XPATH, '(//div[@class="ADXRXN AsRsEE"])[3]//descendant::img')

driver.execute_script('arguments[0].scrollIntoView();',element)
sleep(3)

#clicking
button = driver.find_element(By.XPATH, '(//div[text()="Join Pinterest"])[3]')
driver.execute_script('arguments[0].click();', button)
sleep(3)

driver.quit()
