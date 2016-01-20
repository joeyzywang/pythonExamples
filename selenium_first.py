from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get("http://www.python.org")
assert "Python" in driver.title
print("Title is:  %s" % driver.title)
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print("Page source is: \n %s" % driver.page_source)
driver.close()