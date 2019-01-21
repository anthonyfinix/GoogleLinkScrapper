from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome = webdriver.Chrome("chromedriver.exe")
f = open("links.txt","w+")

# Search term you need to get of
searchkey = "*anthony finix"
counter = 0
searchTill = 10

chrome.get('https://www.google.com/search?q='+searchkey)

while counter < searchTill:

    chrome.implicitly_wait(10)
    time.sleep(5)
    links = chrome.find_elements_by_class_name('iUh30')

    # Print each link
    for link in links:
        print(link.text)
        f.write(link.text+'\n')

    # next page click
    chrome.find_element_by_id('nav').find_element_by_xpath("//td[@class='cur']/following-sibling::td").find_element_by_tag_name('a').click()
    # counter increase
    counter = counter + 1

chrome.close()
f.close()
