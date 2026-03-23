from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/dynamic-properties')
driver.maximize_window()

# wait = WebDriverWait(driver, 6)
# enable_before = driver.find_element(By.ID, 'enableAfter')
# print(enable_before.is_enabled())
#
# enable_btn = wait.until(EC.element_to_be_clickable((By.ID, 'enableAfter')))
#
# if enable_btn.is_enabled():
#     enable_btn.click()
#     print(enable_btn.text)
#
# visible_ele = wait.until(EC.visibility_of_element_located((By.ID, 'visibleAfter')))
# visible_ele.click()

driver.implicitly_wait(5)