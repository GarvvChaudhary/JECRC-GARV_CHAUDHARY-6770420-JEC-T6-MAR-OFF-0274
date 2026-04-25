from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(2)

#-------------------single frame---------------------------
# iframe = driver.find_element(By.ID, "singleframe")
# driver.switch_to.frame(iframe)
# sleep(2)
#
# driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("Aaaaliye re Aaaaliyeeeeeee")
# sleep(5)

#---------------iframe inside iframe---------------------

driver.find_element(By.XPATH, '//a[text()="Iframe with in an Iframe"]').click()

nested_iframe = driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)

inner_iframe = driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('ab toh chalna padega')
sleep(3)

driver.quit()
