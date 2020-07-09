from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"


driver = webdriver.Chrome(PATH)
driver.get("http://covid.gov.pk/")
print(driver.title)
resultvalue = driver.find_element_by_class_name("numanimate")

print ("Number of active cases in 2020 are " + resultvalue.text) 