import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(40)
driver.get("http://asone.udea.edu.co/movi/#/convocatorias")
assert "Movilidad saliente" in driver.title
time.sleep(5) 
check = driver.find_element_by_xpath("//div/label/span[contains(text(), '¿Solo Becas?')]")
driver.execute_script("arguments[0].click();", check)
#//div/input[contains(text(), 'Consultar')]
submit = driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div/div/input")
driver.execute_script("arguments[0].click();", submit)