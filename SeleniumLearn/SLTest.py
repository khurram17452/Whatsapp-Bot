from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#change the path to where the chromedriver is in your pc
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
#the argument no. 1 is for windows users
options.add_argument(r'--user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument(r'--profile-directory=Default')
driver = webdriver.Chrome(PATH, options = options)
driver.get("https://web.whatsapp.com/")
#sleep for 20 seconds is to wait for the webpage to fully load
time.sleep(20)
hsd = '//div[@dir="ltr"][@data-tab="3"]'
smth = driver.find_element_by_xpath(hsd) #to search dynamic objects in a webpage
username = "name" #enter the name of the user you want to send this msg to 
smth.send_keys(username)
time.sleep(2)
smth.send_keys(Keys.RETURN)
time.sleep(2)
hsdd = '//div[@dir="ltr"][@data-tab="1"]'
msgbox = driver.find_element_by_xpath(hsdd)
msg = "message" #this is the message you want to send
count = 0
while count < 10: #edit the number to the number of times you want to send the same message
    msgbox.send_keys(msg)
    msgbox.send_keys(Keys.RETURN)
    count += 1
print("waiting for 10 seconds before quiting")
time.sleep(10)
driver.quit()