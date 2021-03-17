#imports
from selenium import webdriver
import time

#connections
driver = webdriver.Chrome(r'#location of your selenium driver!!!')
driver.get(r'https://web.telegram.org/')

time.sleep(3)

#users
ids = input('enter ids of your contacts with comma: ')
id =ids.split(',')
ids = list(id) 

msg = input('enter message: ')
count = int(input('how many times: '))
time.sleep(2)

#send_msg
for all in ids:
    user = driver.get('https://web.telegram.org/#/im?p=@{}'.format(all))
    time.sleep(1)
    for mg in range(count):
        msg_box = driver.find_element_by_xpath('//div[@class="composer_rich_textarea"]')
        msg_box.send_keys(msg)
        send_button = driver.find_element_by_xpath('//span[@data-content="Send"]')
        send_button.click()

#quit_browser
time.sleep(10)
driver.close()

#end
