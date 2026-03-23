

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
'''
works in selenium, sleep is not recommended in production level environment as it makes the website interaction slower
so we use wait(Synchronization issue).
Implicitly_wait : Wait for a certain amount of time while trying to find an element before throwing an exception.
wait till the element is found
Works globally. 

Explicit_wait: works for a certain amount of time while trying to find an element before throwing an exception. 
wait till the action is performed
Works for a specific element i.e. doesn't work globally.

Fluent_wait: 
'''
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

# driver.get('https://abc.com/')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

#-----------Implicit_Wait---------------
# driver.implicitly_wait(1)
#
# first = driver.find_element(By.XPATH,'(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# print(first.get_attribute('src'))

#-------------Explicit_wait-------------------
# wait_obj = WebDriverWait(driver, 10, poll_frequency= 200)
#
# submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID, 'submit')))
# submit_button.click()

# wait = WebDriverWait(driver, 10)
#
# loading_ele = wait.until(EC.invisibility_of_element_located((By.ID, 'preloader-animated_svg__circle3')))
#
# title_abc = driver.find_element(By.XPATH, '//span[text() = "ABC SHOWS, SPECIALS & MORE"]')
#
# assert 'SPECIALS' in title_abc.text, 'the text not present'
#
# print('working fine')
#
# driver.quit()

multi_drop = driver.find_element(By.ID, 'colors')
select = Select(multi_drop)

if select.is_multiple:
    select.select_by_index(3)
    select.select_by_value('blue')
    select.select_by_visible_text('Red')

print('before deselect:', [i.text for i in select.all_selected_options])
sleep(3)

select.deselect_by_value('blue')

print('after deselect:', [i.text for i in select.all_selected_options])

driver.quit()
