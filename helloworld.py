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
driver.get('https://www.moneycontrol.com/india/stockpricequote/computers-software-medium-small/firstsourcesolutions/FS07')
element = WebDriverWait(driver, 50).until(
EC.presence_of_element_located((By.XPATH, "//*[@id='Bse_Prc_tick_div']"))
)
project_field = driver.find_element_by_xpath('//*[@id="Bse_Prc_tick_div"]')
print (project_field.text)


