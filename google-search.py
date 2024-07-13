from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys

options = Options()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
searchValue = sys.argv[1]



action = ActionChains(driver)

#Google search input element
searchInput = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

#Google Search Button
clickable = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')

# ActionChains
action.send_keys_to_element(searchInput, searchValue).move_to_element(clickable).click(clickable).perform()

# Initialize webDriverWait
wait = WebDriverWait(driver, 10)


elementsWaitedFor = wait.until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'LC20lb')))

for element in elementsWaitedFor:
    print(element.text)