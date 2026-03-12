#Use all the methods for 12-03-2026
from time import sleep

from selenium import webdriver


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options = opts)

driver.get('https://youtube.com/')

print(driver.title)
print(driver.current_url)

driver.maximize_window()
sleep(2)
driver.minimize_window()

driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)

# driver.close()

driver.quit()


