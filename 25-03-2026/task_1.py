### Booking a Flight Ticket
# 1. Open website (ClearTrip)
# 2. Verify the current url
# 3. Select trip type → One Way if not selected
# 4. Enter:
# From city,
# To city,
# Departure date (calendar handling, if next arrow is showing stale element use action chains by moving to arrow then action.click(ele).perform)
# 5. Click Search Flights
# 6. Wait for results page (handle the loading)
# 7. Fetch me the first flight

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.cleartrip.com/')
driver.maximize_window()

assert 'cleartrip' in driver.current_url, 'Wrong url'

wait=WebDriverWait(driver,5)

#popup
wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@class="pb-1 px-1 flex flex-middle nmx-1"]'))).click()

#clicking one way
driver.find_element(By.ID,'oneway').click()
pickup_city=wait.until(ec.presence_of_element_located((By.XPATH,'//input[@placeholder="Where from?"]')))
pickup_city.click()
pickup_city.send_keys('Jaipur')
find_pickup_city=wait.until(ec.element_to_be_clickable((By.XPATH,"//ul[@class='airportList']/descendant::p[contains(text(),'Jaipur')]")))
find_pickup_city.click()

drp_city=wait.until(ec.presence_of_element_located((By.XPATH,'//input[@placeholder="Where to?"]')))
drp_city.click()
drp_city.send_keys('Goa')
find_drp_city=wait.until(ec.visibility_of_element_located((By.XPATH,"//ul[@class='airportList']/descendant::p[contains(text(),'Goa')]")))
find_drp_city.click()

#Departure calender
input_month="April 2026"
input_date='12'
wait.until(ec.element_to_be_clickable((By.XPATH,'//div[@class="sc-aXZVg dSvAMK mr-2 mt-1"]'))).click()
while True:
    Month=wait.until(ec.visibility_of_element_located((By.XPATH,'(//div[@class="DayPicker-Caption"]/div)[2]'))).text
    if input_month in Month:
        wait.until(ec.element_to_be_clickable((By.XPATH,f"(//div[@class='DayPicker-Month'])[2]/descendant::div[text()='{input_date}']"))).click()
        break
    else:
        sleep(5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"svg[data-testid='rightArrow']"))).click()

driver.find_element(By.XPATH,'//button[@class="sc-dhKdcB jkDAfz flex-1"]').click()
first_flight=wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@class="sc-aXZVg"]/descendant::div[@class="sc-aXZVg dczbns mb-2 bg-white"]/descendant::p[2]')))
print("First flight: ",first_flight.text)