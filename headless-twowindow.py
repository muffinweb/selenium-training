from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")

browser = webdriver.Firefox(options=options)
browser.get('https://myhttpheader.com')

# waitFor = WebDriverWait(browser, 10)
# SearchTextBox = waitFor.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"APjFqb\"]")))

browser.save_screenshot('fullscreen3.png')

# current window
firstWindow = browser.current_window_handle

browser.switch_to.new_window('tab')
browser.get('https://eksisozluk.com')

# eksisozluk tab
secondWindow = browser.current_window_handle

browser.save_screenshot('eksisozluk2.png')


# pageSource = browser.page_source
# print(pageSource)
browser.quit()
