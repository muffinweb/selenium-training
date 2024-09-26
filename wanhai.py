from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys

# ------------------------------------------------------ #

# Selenium Driver Options
options = Options()
options.add_experimental_option('detach', True)
# options.add_argument("--headless")

# ------------------------------------------------------ #


# Service URL
serviceURL = "https://www.wanhai.com/views/Main.xhtml"

driver = webdriver.Chrome(options=options)
driver.get(serviceURL)

# Current Window
original_window = driver.current_window_handle

# Print Current Window
print(original_window)

# Initialize webDriverWait
waitForQueryArea = WebDriverWait(driver, 10)

# Wait until queryAreaElement is loaded
queryAreaElementWaitedFor = waitForQueryArea.until(
    expected_conditions.presence_of_all_elements_located((By.ID, 'cargoTrackV2Bean')))

# Initialize ActionChains instance with driver
actions = ActionChains(driver)

# Get Elements to Interact in Original Window
queryInputText = driver.find_element(By.ID, 'q_ref_no1')
queryButton = driver.find_element(By.ID, 'quick_ctnr_query')

# Declare Tracking Number
BLNumber = "052EA06620"

# Write Tracking number to related Input and click to query
(actions.move_to_element(queryInputText)
 .send_keys_to_element(queryInputText, BLNumber)
 .click(queryButton)
 .perform())



# Wait Until New Window Opened
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.number_of_windows_to_be(2))

# Switch to New Window
resultWindow = driver.window_handles[1]
driver.switch_to.window(resultWindow)

# Wait for result page to load
waitForDataArea = WebDriverWait(driver, 30)
waitedForDataArea = wait.until(expected_conditions.presence_of_element_located((By.ID, 'DATA_AREA')))

#
driver.find_element(By.XPATH, '//*[@id="cargoTrackV2Bean"]/table/tbody/tr[2]/td[6]/u[1]/a').click()


# Wait Until New Window Opened
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.number_of_windows_to_be(3))

resultSecondWindow = driver.window_handles[2]
driver.switch_to.window(resultSecondWindow)


waitForSecondDataArea = WebDriverWait(driver, 30)
waitedForSecondDataArea = wait.until(expected_conditions.presence_of_element_located((By.ID, 'DATA_AREA')))

print(driver.page_source)