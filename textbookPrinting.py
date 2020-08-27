from selenium import webdriver
import pdb
import time
#from calNetLogin import calNetLogin
#from refresh import refresh, refresh_win
#from closeTicket import closeTicket
import csv
from getpass import getpass
import pyautogui

username = input("Username: ")
password = getpass("Password: ")

# Login to ServiceNow
driver = webdriver.Firefox()
driver.get("https://etext-ise.pearson.com/courses/5446485/products/127573/pages/120?locale=&platformID=1030")

time.sleep(20)
username_input = driver.find_element_by_id("username")
username_input.send_keys(username)
password_input = driver.find_element_by_id("password")
password_input.send_keys(password)
enter_button = driver.find_element_by_id("mainButton")
enter_button.click()
time.sleep(30)

for i in range(120, 171):
    time.sleep(10)
    driver.find_element_by_id("vega-app-bar-overflow-menu").click()
    driver.find_elements_by_class_name("linkStyle")[0].click()
    time.sleep(5)

    # Click print on save to pdf
    pyautogui.click(320,400)
    time.sleep(5)
    # Click up on scrollbar
    pyautogui.click(150,200)
    time.sleep(1)
    # Click to select on folder
    pyautogui.click(130,360)
    time.sleep(1)
    # Select file name input field
    pyautogui.click(300,620)
    # Input name
    pyautogui.typewrite("intermediate accounting P" + str(i))
    # Click save
    pyautogui.click(1200,690)

    time.sleep(20)
    #pdb.set_trace()
    driver.find_element_by_id("docViewer_ViewContainer_PageContainer_0").click()
    driver.find_elements_by_class_name("navigationBtn")[1].click()

pdb.set_trace()
