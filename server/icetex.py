import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true")
assert "Becas" in driver.title
check = driver.find_element_by_xpath("//*[@id='RBLOpcionBuscar_2']")
check.click()
time.sleep(5)

elems = driver.find_element_by_xpath("//*[@id='Label5']").text
print(len(elems))
elems=elems[(len(elems)-2):(len(elems)-1)]
print(elems)




