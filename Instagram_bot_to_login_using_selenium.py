from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time

w = wd.Chrome()
w.get("https://www.instagram.com")
time.sleep(3)
w.find_element_by_name("username").send_keys("username")
time.sleep(3)
w.find_element_by_name("password").send_keys("password")
time.sleep(3)
w.find_element_by_xpath("//div[@class='                    Igw0E     IwRSH      eGOV_         _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    ']").click()
time.sleep(5)
w.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
time.sleep(3)
w.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()


w.close()
