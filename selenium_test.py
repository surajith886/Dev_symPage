from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("C:/Users/SUROJIT/OneDrive/Desktop/devops/sym_page/index.html")

driver.find_element(By.ID,"name").send_keys("Surajit Halder")
driver.find_element(By.ID,"email").send_keys("test@gmail.com")
driver.find_element(By.ID,"password").send_keys("Urmi@123")
driver.find_element(By.ID,"confirmPassword").send_keys("Urmi@123")

driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]").click()

driver.find_element(By.ID,"course").send_keys("B.Tech")

driver.find_element(By.CLASS_NAME,"btn").click()

time.sleep(5)
driver.quit()