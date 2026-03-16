from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")
driver.maximize_window()

sleep(3)

print("Title:", driver.title)

yes_radio = driver.find_element(By.XPATH, "//label[@for='yesRadio']")

yes_radio.click()
sleep(2)

result = driver.find_element(By.CLASS_NAME, "text-success")
print("Result:", result.text)

print("Class:", yes_radio.get_attribute("class"))
print("For attribute:", yes_radio.get_attribute("for"))

print("URL:", driver.current_url)

driver.quit()