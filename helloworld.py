from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
account_sid = 'AC07605b79ba321cdce3a98a19fa72b19c'
auth_token = '1e28328e5491217338e7cbbbbe103281'
client = Client(account_sid, auth_token)

driver.get('https://www.moneycontrol.com/india/stockpricequote/computers-software-medium-small/firstsourcesolutions/FS07')
i=1
try:
    while(i<10):
            element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='Bse_Prc_tick_div']"))
            )
            project_field = driver.find_element_by_xpath('//*[@id="Bse_Prc_tick_div"]')
            print (project_field.text)
            driver.refresh()
            i=i+1
            time.sleep(2)
            if (i==29):
                message = client.messages.create(
                              body='sdsdsdsdsdwsdfsdwsdsd sedwdswdf!',
                              from_='+18325013393',
                              to='+919066619956'
                          )
                last_sms = client.messages.list()[0]
                print (last_sms.status)
                
            
except:
    print("error")

