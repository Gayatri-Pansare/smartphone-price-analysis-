from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from campusx import chrome_driver

# Define the driver path
driver_path = Service("C:/Users/gayat/OneDrive/Desktop/chromedriver-win64/chromedriver.exe")

#Set the different options for the browser
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",['enable-logging'])

#Ignore the certificate and SSL errors
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Maximize the browser window
chrome_options.add_argument("start-maximized")

# Define the driver and open the browser
chrome_driver = webdriver.Chrome(service= driver_path , options=chrome_options)

#Rest of your code..
chrome_driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

chrome_driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
chrome_driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(1)
chrome_driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/aside/div/div[6]/div[2]/label[1]/input').click()
time.sleep(2)

old_height=chrome_driver.execute_script("return document.body.scrollHeight")
while True:

    chrome_driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    new_height=chrome_driver.execute_script("return document.body.scrollHeight")

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height=new_height

html = chrome_driver.page_source
with open('smartprix.html', 'w', encoding='utf-8') as f:
    f.write(html)






