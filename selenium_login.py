from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.PhantomJS()
driver.get("https://sc.omniture.com/login")

print("Title is:  %s" % driver.title)

company = driver.find_element_by_name('company')
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

company.send_keys("asctestsj")
username.send_keys("zhenwang")
password.send_keys("zhenwang")

driver.find_element_by_id("login_button").click()
WebDriverWait(driver, 20)
print("Title is:  %s" % driver.title)
driver.close()