from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


opts=webdriver.ChromeOptions()
opts.add_argument('--headless')
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.amazon.in/")
sleep(3)

navbar=driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
print(navbar)

logo=driver.find_element(By.CSS_SELECTOR,"#nav-logo-sprites")
print(logo)

cart=driver.find_element(By.CSS_SELECTOR,"#nav-cart")
print(cart)

signin=driver.find_element(By.CSS_SELECTOR,"#nav-tools #nav-link-accountList a")
print(signin)

categories=driver.find_elements(By.CSS_SELECTOR,"#nav-xshop a")
print(f'length of categories is :{len(categories)}')

driver.quit()