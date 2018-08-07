import requests
import time
from selenium import webdriver
 
class Steps:
   
    def __init__(self,schema):
        self.schema = schema
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def getStart(self,schema):
        return schema['start'] 
    
    def getSelector(self,schema):
        return schema['css'] 

    def getFinish(self,schema): 
        return schema['finish']

    def getUrl(self):
        return self.driver.get(self.schema['url']) 

    def getSteps(self): 
        return self.schema['steps']
    
    def getTable(self): 
        return self.schema['table']
    
    def getRow(self): 
        return self.schema['rows']
        
    def getTitle(self): 
        return self.schema['title']
   
    def main_steps(self,steps): 
        for index,val in steps.items():
            self.click_css(val['css'])

    def getSchemaString(self, i, schema):
        return (self.getStart(schema)+str(i)+self.getFinish(schema))
    
    def table_steps(self): 
        table = self.driver.find_elements_by_css_selector(self.getSelector(self.getTable()))
        for i in range(len(table)):
            self.getUrl()
            self.main_steps(step.getSteps())
            table_string = str(self.getSchemaString(i+1, self.getTable()))
            print("Tabla #: "+str(i+1)+" Evento Tabla: "+ table_string)
            self.rows_steps(table_string,i)
     
    def rows_steps(self,string,i):
        row = self.driver.find_elements_by_css_selector(self.getSelector(self.getRow()))
        for r in range(len(row)):
            self.getUrl()
            self.main_steps(step.getSteps())
            rows_string = str(self.getSchemaString(r, self.getRow()))
            if (i==0):
                self.driver.execute_script("location.reload();")
            else: 
                self.driver.execute_script(string)
            self.driver.execute_script(rows_string)
            print("Fila #: "+str(r+1)+" Convocatoria: "+self.driver.find_element_by_css_selector("#LblInfoConvocatoria").text + " Evento JS: " + rows_string )
                
        
    def click_css(self,selector):
        self.driver.find_element_by_css_selector(str(selector)).click()
        time.sleep(1)

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
        "css": "#GVConvocatorias > tbody > tr:nth-child(12) > td > table > tbody > tr > td", 
        "start":"__doPostBack('GVConvocatorias','Page$",
        "finish":"')"
    },
    "rows":{
        "css":"#GVConvocatorias > tbody > tr > td:nth-child(1) > a",
        "start":"__doPostBack('GVConvocatorias','$",
        "finish":"')"
    }
}
 
step = Steps(icetex)
step.getUrl()
step.main_steps(step.getSteps())
step.table_steps()