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

songs_list = driver.find_element(By.ID, 'songs')
select = Select(songs_list)

l1=[i.text for i in select.options]
for song in l1 :
    if ('girl' in song.lower() or 'love' in song.lower() ):
        select.select_by_visible_text(song)


button=driver.find_element(By.XPATH,"//button[text()='Add to Playlist']")
button.click()

sleep(6)

driver.quit()
