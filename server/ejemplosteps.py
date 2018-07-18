import requests
import time
from selenium import webdriver
 
class Steps:
   
    def __init__(self,schema):
        self.schema = schema
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def getUrl(self):
        return self.driver.get(self.schema['url']) 

    def getSteps(self): 
        return self.schema['steps']
    
    def getTable(self): 
        return self.schema['table']
    
    def getRow(self): 
        return self.schema['rows']
    
    def getSelector(self, n, ruta):
        selector = str(ruta[1])+str(n)+str(ruta[2])
        return str(selector)
        
    def getTitle(self): 
        return self.schema['title']
   
    def main_steps(self,steps): 
        for index,val in steps.items(): 
            #css selector se recupera del Json
            self.click_css(val['css'])

    def links_steps(self, ruta): 
        n = ruta['starts']
        for n in range(ruta['finish']-1): 
            #css selector se recupera del Json
            self.click_css(self.getSelector((n+ruta['starts']),ruta))
            self.getUrl()
            self.main_steps(self.getSteps())
            
    def click_css(self,selector):
        self.driver.find_element_by_css_selector(str(selector)).click()
        time.sleep(3)

    def test_page(self):
        #URL viene del JSON        
        self.getUrl()
        #title viene del JSON para verificar que la página no sea 404
        assert str(self.getTitle()) in self.driver.title
        self.main_steps(self.getSteps())
        self.links_steps(self.getRow())

icetex = {
    "url": "https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true",
    "title":"Convocatorias de Becas",
    "steps": {
        1: {
            "event": "click",
            "css": "#RBLOpcionBuscar_2"
        }
    },
    "table":{
        1: "td:nth-child(",
        2: ") > a",
        "starts": 2,
        "finish": 8
    }, 
    "rows":{
        1: "tr:nth-child(",
        2: ") > td:nth-child(1) > a",
        "starts":2,
        "finish":11
    }    
}
 
step = Steps(icetex)
step.test_page()