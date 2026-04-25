from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(2)

# parent_window = driver.current_window_handle
# print(driver.current_window_handle)
#
# driver.find_element(By.XPATH, '//a[text()="Click Here"]').click()
# sleep(2)
#
# all_windows = driver.window_handles
# print(len(all_windows))
#
# driver.switch_to.window(all_windows[-1])
# print(driver.current_window_handle)
#
# assert 'New' in driver.find_element(By.CLASS_NAME, 'example').text
# # print('done')
# driver.close()
# sleep(3)
# driver.switch_to.window(parent_window)
# print(driver.current_window_handle)
# sleep(2)

#-------------------opening a website in new window----------------
driver.switch_to.new_window('window')
sleep(2)
driver.get('https://www.youtube.com/')
sleep(3)

'''we can use('tab') to open the new website in a new tab but in the same window'''

driver.switch_to.new_window('tab')
sleep(2)
driver.get('https://www.youtube.com/')
sleep(3)

driver.quit()