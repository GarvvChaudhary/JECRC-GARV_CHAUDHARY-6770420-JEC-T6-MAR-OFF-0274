from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get("https://the-internet.herokuapp.com/login")

xpath_name=driver.find_element(By.XPATH,"//input[@name='username']")
print(xpath_name)

xpath_pass=driver.find_element(By.XPATH,"//input[@id='password']")
print(xpath_pass)

xpath_button=driver.find_element(By.XPATH,"//button[@type]")
print(xpath_button)

xpath_element=driver.find_element(By.XPATH,'//a[text()="Elemental Selenium"]')
print(xpath_element)

xpath_login=driver.find_element(By.XPATH,"//h2[contains(text(),'Login Page')]")
print(xpath_login)