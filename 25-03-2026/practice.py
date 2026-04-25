# Complete Flow On Amazon
# Steps:
# Open website
# Verify homepage title & URL
# Search for product → "Headphones"
# Apply filters (Brand,price(upto 500 or above 1000 anything))
# Open a product → switch to new tab
# Verify product details (title, price) using assert
# Add to cart
# Go to cart verify item (using assert with the name used earlier)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()

assert 'amazon' in driver.current_url, 'Error'

wait=WebDriverWait(driver,5)
searchbox=wait.until(ec.visibility_of_element_located((By.ID,'twotabsearchtextbox')))
searchbox.send_keys('Headphones')

driver.find_element(By.ID,'nav-search-submit-button').click()

driver.find_element(By.XPATH,'//ul[@id="filter-p_123"]/descendant::li[3]').click()
driver.find_element(By.XPATH,'//div[@id="priceRefinements"]/descendant::a[6]').click()

new_product=wait.until(ec.presence_of_element_located((By.XPATH,'//div[@role="listitem"]/descendant::h2/span')))
product_title=new_product.text
new_product.click()

product_price=wait.until(ec.presence_of_element_located((By.XPATH,'//span[@class="a-price"]/span[@class="a-offscreen"]'))).text

all_windows=driver.window_handles
driver.switch_to.window(all_windows[-1])

assert product_title in driver.find_element(By.XPATH,'//span[@id="productTitle"]').text,'Product not found'
assert product_price in driver.find_element(By.XPATH,"//div[@id='apex_desktop']/descendant::span[@class='a-price-whole']").text, 'Product not found'

cart_button=wait.until(ec.presence_of_element_located((By.ID,'add-to-cart-button')))
cart_button.click()
cart=wait.until(ec.presence_of_element_located((By.ID,'nav-cart')))
cart.click()

assert product_title in wait.until(ec.presence_of_element_located((By.XPATH,'//span[@class="a-truncate-full a-offscreen"]'))).get_attribute('textContent'), 'Wrong Product'
assert product_price in wait.until(ec.presence_of_element_located((By.XPATH,'//div[@class="sc-badge-price sc-apex-cart-price"]/descendant::span[@class="a-offscreen"]'))).text, 'Wrong product'
sleep(2)