from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(2)

arama = driver.find_element(By.NAME, "q")
arama.send_keys("Python freelance jobs")
arama.send_keys(Keys.RETURN)

time.sleep(3)

driver.save_screenshot("google_arama_sonucu.png")

print("Ekran görüntüsü alındı!")

time.sleep(2)
input("Kapatmak için Enter'a bas...")