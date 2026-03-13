from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.cricbuzz.com")
sleep(5)

css1 = driver.find_element(By.CSS_SELECTOR,"a[title='Live Cricket Score']")
print("CSS selectors working")
print(css1)
css2 = driver.find_element(By.CSS_SELECTOR,"a[title='Cricket Schedule']")
print("CSS selectors working")
print(css2)
css3 = driver.find_element(By.CSS_SELECTOR,"a[title='Cricket Series']")
print("CSS selectors working")
print(css3)

print("CSS selectors working")



x1 = driver.find_element(By.XPATH,"//a[@title='Live Cricket Score']")
print("XPath attribute working")
print(x1)
x2 = driver.find_element(By.XPATH,"//a[@title='Cricket Schedule']")
print("XPath attribute working")
print(x2)
x3 = driver.find_element(By.XPATH,"//a[@title='Cricket Series']")
print("XPath attribute working")
print(x3)

print("XPath attribute working")



t1 = driver.find_element(By.XPATH,"//a[text()='Series']")
print("XPath inner text working")
print(t1)
t2 = driver.find_element(By.XPATH,"//a[text()='Teams']")
print("XPath inner text working")
print(t2)
t3 = driver.find_element(By.XPATH,"//a[text()='News']")
print("XPath inner text working")
print(t3)

print("XPath inner text working")


sleep(3)
driver.quit()