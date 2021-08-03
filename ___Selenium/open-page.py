from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='C:/Users/Oğuz KABA/Documents/GitHub/python_projects/___Selenium/chromedriver.exe')

url="http://github.com/oguzkaba"

driver.get(url)

time.sleep(2)
print(driver.title)
time.sleep(2)
driver.close()
