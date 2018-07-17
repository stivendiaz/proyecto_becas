from requests import get
from bs4 import BeautifulSoup as soup

class StepsParser:
    def __init__(self, tree, schema):
        self.tree = tree
        self.schema = schema

    def parse(self):
        return { 'title': self.getTitle(), 'description' : self.getDescription(),'img':self.getImg(),'mas_info':self.getMas_info()}

    def getTitle(self):
        title = self.tree.select_one(self.schema['title'])
        return title.string

    def getDescription(self):
        description = self.tree.select_one(self.schema['description'])
        return description.text
    
    def getImg(self):
        img = self.tree.select_one(self.schema['img'])
        return img['src']

    def getMas_info(self):
        link = self.tree.select_one(self.schema['mas_info'])
        return link['href']

def getHtml(url):
    response = get(url)
    return response.text

def getParser(html):
    return soup(html, 'html.parser')

def getSteps(parser, schema):
    return parser.select(schema['discriminator'])

def scrap(schema):
    html = getHtml(schema['url'])
    parser = getParser(html)
    for tree in getSteps(parser, schema):
        stepsParser = StepsParser(tree, schema)
        print(stepsParser.parse())

cursosEnColombia = {
    'url': 'https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true',
    'steps':{
    'event': 'click',
    'xpath': "//*[@id='RBLOpcionBuscar_2']"}
}