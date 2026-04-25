import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
sleep(2)

wait = WebDriverWait(driver, 10)

#----------------------------simple JS alert-----------------------------------
# simple = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Click for JS Alert"]')))
# simple.click()
#
# alert = driver.switch_to.alert
# alert.accept()
# sleep(2)

#----------------------confirmation alert------------------------
# simple = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Click for JS Confirm"]')))
# simple.click()
# sleep(2)
#
# alert = driver.switch_to.alert
# # alert.accept()
# alert.dismiss()
# sleep(2)

#------------------Prompt alert---------------------
# simple = wait.until(EC.((By.XPATH, '//button[text()="Click for JS Prompt"]')))
# simple.click()
# sleep(2)
#
# alert = driver.switch_to.alert
# alert.send_keys("Hello 1")
# # alert.accept()
# alert.dismiss()
# sleep(2)

#-----------------switching to alerts using wait------------
wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Click for JS Alert"]')))
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
sleep(2)

driver.quit()
