from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
col_name = ['url']
df_url = pd.read_csv("links.txt", names=col_name)

while True:
    website_random_URL = random.sample(df_url.url.to_list(), 1)

    driver.get(website_random_URL[0])
    time.sleep(5)
    height = int(driver.execute_script("return document.documentElement.scrollHeight"))

    while True:
        driver.execute_script('window.scrollBy(0,10)')
        time.sleep(0.10)
        totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
        
        if totalScrolledHeight == height:
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            driver.switch_to.window(driver.window_handles[0])
            break
    print('***Web Page Visited***')
