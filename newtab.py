from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

## This option object will be used as parameter argument to stay browser active
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url = 'https://www.google.com'
browser = webdriver.Chrome(options=chrome_options)

# First URL to visit
browser.get(url)

# Get Current Window
original_window = browser.current_window_handle
print(original_window)

## switch_to.new_window('tab <==') or switch_to.new_window('window <==') are options
## Argument tab triggers openning tab, argument window triggers openning new window
browser.switch_to.new_window('window')
browser.get('https://www.facebook.com')

#Facebook page tab
second_window = browser.current_window_handle

print(second_window)

browser.switch_to.window(original_window)

browser.implicitly_wait(10)

print('Process successful')