#Add url and title methods for each browser

from selenium import webdriver

browsers = ['Chrome', 'Edge', 'Firefox']

for item in browsers:

    if item == 'Chrome':
        driver = webdriver.Chrome()

    elif item == 'Edge':
        driver = webdriver.Edge()

    elif item == 'Firefox':
        driver = webdriver.Firefox()

    driver.get("https://www.google.com")

    print(driver.title)
    print(driver.current_url)

    driver.close()