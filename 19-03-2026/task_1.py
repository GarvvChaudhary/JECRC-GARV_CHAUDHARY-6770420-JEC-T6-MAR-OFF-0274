from asyncio import wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com/')
driver.maximize_window()

circle_obj = WebDriverWait(driver, 2)

images = circle_obj.until(EC.presence_of_all_elements_located((By.XPATH, '//section[@class="tilegroup tilegroup--homehero tilegroup--landscape"]/descendant::picture/img')))

for image_link in images:
    print(image_link.get_attribute('src'))

# circle_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="hero__arrow hero__arrow-right"]')))
# circle_button.click()
#
# driver.implicitly_wait(1)
#
# first = driver.find_element(By.XPATH,'//div[@class="tile--hero__container"]')
# print(first.get_attribute('src'))

driver.quit()
