from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true")
assert "Becas" in driver.title
elem = driver.find_element_by_xpath("//*[@id='RBLOpcionBuscar_2']")
elem.click()

