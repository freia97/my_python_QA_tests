from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"
path = "C:/chromedriver.exe"

try:
    driver = webdriver.Chrome(path)
    driver.get(link)

    input1 = driver.find_element_by_css_selector("body > div > form > div:nth-child(1) > input")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_css_selector("body > div > form > div:nth-child(2) > input")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_css_selector("body > div > form > div:nth-child(3) > input")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_css_selector("#country")
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    driver.quit()
