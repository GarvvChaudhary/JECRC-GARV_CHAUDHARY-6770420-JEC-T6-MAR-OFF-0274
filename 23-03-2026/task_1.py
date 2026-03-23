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
driver.get('https://www.royalchallengers.com/')
driver.maximize_window()
sleep(3)

action = ActionChains(driver)
logo = driver.find_element(By.XPATH, '//img[@alt="Jio"]')
action.scroll_to_element(logo).perform()
sleep(3)

for i in range(0,5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(2)

sleep(5)

driver.quit()
