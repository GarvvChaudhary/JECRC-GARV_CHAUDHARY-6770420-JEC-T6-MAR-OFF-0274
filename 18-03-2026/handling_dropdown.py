from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver  = webdriver.Chrome(options=opts)

# driver.get('https://testautomationpractice.blogspot.com/')
driver.get('https://www.lenskart.com/sunglasses.html')
driver.maximize_window()


# country_dropdown = driver.find_element(By.ID, 'country')
# dropdown = Select(country_dropdown)

# dropdown.select_by_value('australia')
# sleep(2)
# dropdown.select_by_index(4)
# sleep(3)
# dropdown.select_by_visible_text('Japan')
# sleep(5)

sort_dropdown = driver.find_element(By.ID, 'sortByDropdown')
dropdown = Select(sort_dropdown)

# dropdown.select_by_value('created')
# sleep(5)
dropdown.select_by_value('best_sellers')
sleep(5)

first = driver.find_element(By.XPATH, "(//div[@id='listing-wrapper']//div[@data-cy = 'plpCardContainer'])[1]")
print(first.text)
sleep(5)

driver.quit()
