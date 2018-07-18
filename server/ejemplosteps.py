import requests
import time
from selenium import webdriver
 
class Steps:
   
    def __init__(self,schema):
        self.schema = schema
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
                 
    def test_page(self):
        #URL viene del JSON        
        self.driver.get(self.schema['url']) 
        steps_schema = self.schema['steps']
        
        for n in steps_schema: 
            #id viene del JSON para verificar que la página no sea 404
            assert str(self.schema['steps'][n]['id']) in self.driver.title
            #css selector se recupera del Json  
            pasos = str(self.schema['steps'][n]['css'])
            self.click_css(pasos)

    def click_css(self,selector):
        self.driver.find_element_by_css_selector(str(selector)).click()
        time.sleep(10)
 
icetex = {
    "url": "https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true",
    "steps": {
        1: {
            "id": "Convocatorias de Becas",
            "event": "click",
            "css": "#RBLOpcionBuscar_0"
        },
        2: {
            "id": "Convocatorias de Becas",
            "event": "click",
            "css": "#RBLOpcionBuscar_1"
        },
        3: {
            "id": "Convocatorias de Becas",
            "event": "click",
            "css": "#RBLOpcionBuscar_2"
        }
    }
}
 
step = Steps(icetex)
step.test_page()