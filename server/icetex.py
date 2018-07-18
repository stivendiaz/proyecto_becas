from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true")
assert "Beco" in driver.title
check = driver.find_element_by_xpath("//*[@id='RBLOpcionBuscar_2']")
check.click()




