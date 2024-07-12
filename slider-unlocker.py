from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Options Object will be used as an argument to change some default settings
chrome_options = Options()

# Adding this argument to make browser open even test-script is done
chrome_options.add_experimental_option("detach", True)

#Create browser/driver instance
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

# open tab and visit url argument one
browser.get('http://slider.test')

# get it's title
appTitle = browser.title

# print title to terminal output
print(appTitle)

#elements
ui_slider = browser.find_element(By.CLASS_NAME, 'ui-slider-handle')
resultElem = browser.find_element(By.TAG_NAME, 'h3')

actions = ActionChains(browser, duration=1)

actions.move_to_element(ui_slider).click_and_hold(ui_slider)

for i in range(400):
    actions.move_by_offset(1, 0)

actions.release()
actions.perform()
