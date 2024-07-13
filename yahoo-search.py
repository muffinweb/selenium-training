from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from sys import argv

# Url to visit
url = 'https://yahoo.com'

## Adding behaviour argument to firefox a little bit different from Chrome one
options = Options()
options.set_preference('detach', True)

#Default Search Value
searchValue = ''


## Search argument starts from index one we need to iterate and combine them all into one sentence
if(len(argv) > 1):
    del argv[0]
    searchValue = ' '.join(argv)

#Initialize Browser/Driver
browser = webdriver.Firefox(options=options)

# Visit Url
browser.get(url)

allWindows = []

# get original window id
origWindow = browser.current_window_handle

allWindows.append(origWindow)

## In browser all tabs/windows count is equal to One?
assert len(browser.window_handles) == 1

# Elements to
searchInput = browser.find_element(By.ID, 'ybar-sbq')
searchButton = browser.find_element(By.ID, 'ybar-search')

# Initialize Action queue instance
actions = ActionChains(browser)

# Action for searching..
actions.move_to_element(searchInput)\
    .send_keys(searchValue)\
    .move_to_element(searchButton)\
    .click(searchButton)\
    .perform()

wait = WebDriverWait(browser, 30)

wait.until(EC.number_of_windows_to_be(2))


for window_handle in browser.window_handles:
    if(window_handle != origWindow):
        allWindows.append(window_handle)

print(allWindows)
browser.quit()