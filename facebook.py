from selenium import webdriver

#Initialize Browser Driver
browser = webdriver.Chrome()

#Define Url to visit
url = 'https://www.facebook.com'

#Visit Url
browser.get(url)

#Get Visited Url's Title
webapp_title = browser.title

#Print Result
print(webapp_title)

#Quit Browser
browser.quit()