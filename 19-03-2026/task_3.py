'''TASK 3
1. navigate to amazon
2. search a product through send_keys
BUT dont click on search or keys.enter
3. Wait for the suggestions to appear
4. Click on 4th suggestion
5. Click on Sort By and click on newest
6. Click on free shipping check box
7. wait for first product and return me the name&price
(without using inner text)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.amazon.in")
driver.maximize_window()

search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("laptop")

suggestions = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"s-suggestion")]')))
suggestions[4].click()

sort_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
sort_dropdown.click()

newest_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Newest")]')))
newest_option.click()

free_shipping = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Free Shipping"]')))
free_shipping.click()
sleep(2)

product = wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@data-component-type="s-search-result"])[1]')))

name = product.find_element(By.XPATH, '//h2').get_attribute("innerHTML")
price = product.find_element(By.XPATH, './/span[@class="a-price-whole"]').get_attribute("innerHTML")

print("Product:", name)
print("Price:", price)

driver.quit()