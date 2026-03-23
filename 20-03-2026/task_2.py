from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

opts = webdriver.ChromeOptions()

opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get(r'S:\Capgemini\Selenium\playlist.html')
driver.maximize_window()

song_list = driver.find_element(By.ID, 'songs')
select = Select(song_list)

fav = input("enter your fav artist: ")

songs = driver.find_elements(By.XPATH, f'//optgroup[@label="{fav}"]/option')
for song in songs:
    print(song.text)
    select.select_by_visible_text(song.text)

button = driver.find_element(By.XPATH, "//button[text()='Add to Playlist']")
button.click()

sleep(6)
driver.quit()