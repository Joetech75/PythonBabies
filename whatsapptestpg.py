import os
from selenium import webdriver as w
from webdriver_manager.chrome import ChromeDriverManager
#import chromedriver_binary

driver = w.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
name = input('Enter the name of the person or whatsapp group : ')
msg = input('Enter the count of messages : ')
count = int(input('Enter the count : ')) 

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
   msg_box.send_keys(msg)
   button = driver.find_element_by_class_name('_3M-N-')
   button.click()

