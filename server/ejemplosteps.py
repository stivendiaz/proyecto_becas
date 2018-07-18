import requests
import time
from selenium import webdriver
 
class Steps:
   
    def __init__(self,schema):
        self.schema = schema
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def getSteps(self): 
        return self.schema['steps']

    def getTitle(self): 
        return self.schema['title']
    
    def getCss(self, n): 
        return self.schema['steps'][n]['css']
        
    def main_steps(self,steps): 
        for n in steps: 
            #css selector se recupera del Json
            self.click_css(self.getCss(n))

    def click_css(self,selector):
        self.driver.find_element_by_css_selector(str(selector)).click()
        time.sleep(3)

    def test_page(self):
        #URL viene del JSON        
        self.driver.get(self.schema['url']) 
        #title viene del JSON para verificar que la página no sea 404
        assert str(self.getTitle()) in self.driver.title
        self.main_steps(self.getSteps())

icetex = {
    "url": "https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true",
    "title":"Convocatorias de Becas",
    "steps": {
        1: {
            "event": "click",
            "css": "#RBLOpcionBuscar_2"
        }
    },
    "links": {
            "rows_css": "td:nth-child(1) > a",
            "table_css": "td:nth-child(2) > a"
    }      
}
 
step = Steps(icetex)
step.test_page()