from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
# driver.get('https://demoqa.com/droppable')
# driver.maximize_window()
# sleep(2)
#
# action = ActionChains(driver)
# wait  = WebDriverWait(driver, 10)
#------------Simple drag&drop------------
# drag_box = driver.find_element(By.ID, 'draggable')
# drop_box = driver.find_element(By.ID, 'droppable')
# sleep(2)
#
# action.drag_and_drop(drag_box, drop_box).perform()
# sleep(3)

#--------------Prevent propagation---------------------

# button = driver.find_element(By.XPATH, '//button[@id="droppableExample-tab-preventPropogation"]')
# button.click()
# sleep(2)
#
# drag_box = wait.until(EC.visibility_of_element_located((By.ID, 'dragBox')))
# drop_box = driver.find_element(By.ID, 'greedyDropBoxInner')
# sleep(2)
#
# action.drag_and_drop(drag_box, drop_box).perform()
# sleep(3)


#----------------------Scrolling to element----------------------------------------------
# driver.get('https://supertails.com/')
# driver.maximize_window()
#
# actions = ActionChains(driver)
#
# persian_cat = driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
# actions.scroll_to_element(persian_cat).perform()
# sleep(5)
#
# actions.scroll_by_amount(0,-1500).perform()
# sleep(2)
#


'''
click() is left click
context_click() is the right click
double_click() is double click
'''

#--------------------------Keyboard Actions------------------------------------

# driver.get('https://supertails.com/')
# driver.maximize_window()
# sleep(2)
# action = ActionChains(driver)

# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(5)
# action.send_keys(Keys.PAGE_UP).perform()
# sleep(5)

# action.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(3)
# action.key_up(Keys.CONTROL).perform()
# sleep(3)

# driver.get(r'S:\Capgemini\Selenium\Assignment\23-03-2026\address_fields.html')
# driver.maximize_window()
# sleep(2)
# action = ActionChains(driver)
# present = driver.find_element(By.ID, 'presentAddress')
# permanent = driver.find_element(By.ID, 'permanentAddress')
#
# present.send_keys('JECRC,JAIPUR,HARYANA,RAJASTHAN')
# sleep(2)
# present.click()
#
# action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(2)
# action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# sleep(2)
#
# action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(5)

driver.get(r'S:\Capgemini\Selenium\Assignment\23-03-2026\index1.html')
driver.maximize_window()

action = ActionChains(driver)

driver.find_element(By.ID, 'password').send_keys('shadowdagger')
sleep(3)

show_pwd = driver.find_element(By.ID, 'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(5)

action.release().perform()
sleep(5)

driver.quit()