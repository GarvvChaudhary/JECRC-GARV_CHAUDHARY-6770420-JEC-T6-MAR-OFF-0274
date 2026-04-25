## Task 1

### https://codepen.io/gdw96/pen/jOypoYL
'''
1. navigate to the above url
2. enter username and password
3. click on hold on the eye to view password
4. click on register
5. Use sleep for 5sec then refresh the page
6. Validate the word `Registration` using assert
---
'''

driver=webdriver.Chrome()
actions=ActionChains(driver)
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()
sleep(3)

username=driver.find_element(By.XPATH,"//input[@id='username']")
username.clear()
username.send_keys("Jaskirat")

email=driver.find_element(By.XPATH,"//input[@id='email']")
email.clear()
email.send_keys("Jasi@gmail.com")

password=driver.find_element(By.XPATH,"//input[@id='password']")
password.clear()
password.send_keys("psswrd123")

eyebtn=driver.find_element(By.XPATH,"//button[@id='showPsswd']")
actions.click_and_hold(eyebtn).perform()

registerbtn=driver.find_element(By.XPATH,"//input[@type='submit']")
registerbtn.click()

sleep(5)

#driver.refresh()
driver.back()

iframe=driver.find_element(By.ID,'result')
driver.switch_to.frame(iframe)

element=driver.find_element(By.TAG_NAME,"h1")
assert 'Registration' in element.text, "Retry Registration"
print("Registration successful")


