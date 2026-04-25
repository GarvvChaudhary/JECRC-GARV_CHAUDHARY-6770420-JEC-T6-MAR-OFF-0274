'''
1. navigate to the url: `https://demoqa.com/alerts`
2. work on all the 4 alerts one after the other
3. validate the result appearing, eg: for `ok` you should assert with it the result shown
---

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
wait=WebDriverWait(driver,5)
driver.maximize_window()
sleep(2)

#alert button
driver.find_element(By.ID,'alertButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()

#timer alert
driver.find_element(By.ID,'timerAlertButton').click()
sleep(2)
alert=wait.until(EC.alert_is_present())
alert.accept()

#confirm alert
driver.find_element(By.ID,'confirmButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()
msg=driver.find_element(By.XPATH,'(//div[@class="col-md-6"])[3]/span[2]')
assert 'Ok' in msg.text, 'Error Found'

#dismissing alert
driver.find_element(By.ID,'confirmButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.dismiss()
msg=driver.find_element(By.XPATH,'(//div[@class="col-md-6"])[3]/span[2]')
assert 'Cancel' in msg.text, 'Error found'

#prompt alert
driver.find_element(By.ID,'promtButton').click()
alert=driver.switch_to.alert
sleep(2)
alert.send_keys('alert')
alert.accept()
msg=driver.find_element(By.ID,'promptResult')
assert 'alert' in msg.text,'Error Found'

driver.find_element(By.ID,'promtButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.dismiss()

sleep(2)
driver.quit()
