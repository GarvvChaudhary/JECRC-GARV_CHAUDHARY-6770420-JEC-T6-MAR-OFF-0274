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

folder = os.path.join(os.getcwd(), 'screenshots')
os.makedirs(folder, exist_ok=True)

action = ActionChains(driver)

driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(2)

# driver.save_screenshot(f'{folder}/full_page.png')
# sleep(3)

element = driver.find_element(By.XPATH, '(//div[@class="ADXRXN AsRsEE"])[3]//descendant::img')
action.scroll_to_element(element).perform()
sleep(2)

element.screenshot(f'{folder}/cherry_red.png')
sleep(2)