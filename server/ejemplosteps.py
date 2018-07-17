import requests
import unittest
import time
from selenium import webdriver

class Steps(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) 
                 
    def test_page(self):
        #URL viene del JSON
        self.driver.get("https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true")
        #id viene del JSON para verificar que la página no sea 404
        assert "Becas" in self.driver.title
        #css selector se recupera del Json
        self.checkBox = self.driver.find_element_by_css_selector("#RBLOpcionBuscar_2")
        self.checkBox.click() 
        time.sleep(10)

if __name__ == '__main__':
    	unittest.main()

icetex = {
    "url": "https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true",
    "steps": {
        "1": {
            "id": "Convocatorias de Becas",
            "event": "click", 
            "css": "//*[@id='RBLOpcionBuscar_2']"}
        
    },
}
