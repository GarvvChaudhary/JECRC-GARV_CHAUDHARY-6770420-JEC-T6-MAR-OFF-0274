from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

#--------------------------Drag&Drop------------------------------
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(4)
#
# action = ActionChains(driver)
#
# origin_element = driver.find_element(By.ID, 'column-a')
# target_element = driver.find_element(By.ID, 'column-b')
#
# action.drag_and_drop(origin_element, target_element).perform()
# sleep(5)

#-------------------------MouseHovering-----------------------------
driver.get('https://supertails.com/')
driver.maximize_window()

action = ActionChains(driver)

dogs_hover = driver.find_element(By.XPATH, '(//span[contains(text(), "Dogs")])[1]')
sleep(2)
action.move_to_element(dogs_hover).perform()
sleep(4)

driver.quit()