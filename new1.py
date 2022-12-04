from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver_chrome = webdriver.Chrome()


url = "https://opensource-demo.orangehrmlive.com/"
driver_chrome.get(url)
time.sleep(2)
driver_chrome.maximize_window()
#Login to page

#username
driver_chrome.find_element(By.NAME, "username").send_keys("Admin")
#password
driver_chrome.find_element(By.NAME, "password").send_keys("admin123")
#login button
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#Navigate to pim
time.sleep(5)
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()

#Add Employ button
time.sleep(3)
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()

#Detail of Employ
time.sleep(3)
#firstname
driver_chrome.find_element(By.NAME, "firstName").send_keys("Raj")
#lastname
driver_chrome.find_element(By.NAME, "lastName").send_keys("Kumar")
#employ id
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys("0258")
#save button
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()


#Navigate to Admin
time.sleep(4)
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
#Add User
time.sleep(3)
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()

#User Detail
time.sleep(3)
#admin dropdown
driver_chrome.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div").click()
Element = driver_chrome.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]")
#print(len(Element))
for opt in Element:
    if opt.text == "Admin":
        opt.click()
        break
time.sleep(3)
#select employ name
act=ActionChains(driver_chrome)
driver_chrome.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Raj Kumar")
act.move_to_element(driver_chrome.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role='listbox']"))
time.sleep(3)
Search_Element=driver_chrome.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role='listbox']/div")
for cho in Search_Element:
    if cho.text=="Raj Kumar":
        cho.click()
        break
#select Enabled
driver_chrome.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
Element_ele=driver_chrome.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]")
#print(len(Element_ele))
for obj in Element_ele:
    if obj.text == "Enabled":
        obj.click()
        break
#username input
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("kumar")
#creat password
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Raj1234@")
#confr password
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Raj1234@")
time.sleep(2)
#save button
driver_chrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()

# search employ
time.sleep(3)
#user manage
driver_chrome.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
time.sleep(5)
#user name in search
driver_chrome.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("kumar")
time.sleep(3)
#click search button
driver_chrome.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()

#logout
time.sleep(4)
driver_chrome.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
driver_chrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()


#login
time.sleep(4)
#created user name
driver_chrome.find_element(By.NAME, "username").send_keys("kumar")
#created password
driver_chrome.find_element(By.NAME, "password").send_keys("Raj1234@")
#click login
driver_chrome.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()





