from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(3)

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

women = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-group="women"]')))
action.move_to_element(women).perform()
sleep(5)

tops = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Tops"]')))
tops.click()
sleep(5)

product = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@class="results-base"]/descendant::li[23]')))
action.scroll_to_element(product).perform()
sleep(5)

driver.quit()
