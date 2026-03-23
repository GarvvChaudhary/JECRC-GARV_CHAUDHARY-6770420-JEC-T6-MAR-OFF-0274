from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait = WebDriverWait(driver, 5)

name = wait.until(EC.visibility_of_element_located((By.ID, "username")))
name.send_keys("Garv Chaudhary")

email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
email.send_keys("gabbarsignh@hotmail.com")

phone = wait.until(EC.visibility_of_element_located((By.ID, "tel")))
phone.send_keys("1234567890")


add_file = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="datafile"]')))
add_file.send_keys(r"C:\Users\garvc\OneDrive\Pictures\Screenshots\Screenshot 2026-03-12 195450.png")

gender = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@name="sgender"]'))))
gender.select_by_value("male")

experience = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="experience" and @value="two"]')))
experience.click()

skills = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="ip" and @value="automationtesting"]')))
skills.click()

tools = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="tools"]'))))
tools.select_by_value("selenium")

sleep(5)

submit = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
submit.click()
print("Form Submitted Successfully ;)")
sleep(3)

driver.quit()

