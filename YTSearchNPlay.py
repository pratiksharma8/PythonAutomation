from selenium import webdriver
import time

# print("This program only plays the first suggestion on YouTube \n")
# key = input("What do you want to search?")
key = "Your Search Here"

driver = webdriver.Chrome('/Users/pratik/Desktop/Fun Automation/chromedriver')
driver.get('https://www.youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys(key)

searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()

time.sleep(2)

play = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
play.click()
