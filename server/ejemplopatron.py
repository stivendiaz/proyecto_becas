from requests import get
from bs4 import BeautifulSoup as soup

class ScholarshipParser:
    def __init__(self, tree, schema):
        self.tree = tree
        self.schema = schema

    def parse(self):
        return { 'title': self.getTitle(), 'description' : self.getDescription(),'img':self.getImg()}

    def getTitle(self):
        title = self.tree.select_one(self.schema['title'])
        return title.string

    def getDescription(self):
        description = self.tree.select_one(self.schema['description'])
        return description.text
    
    def getImg(self):
        img = self.tree.select_one(self.schema['img'])
        return img['src']

def getHtml(url):
    response = get(url)
    return response.text

def getParser(html):
    return soup(html, 'html.parser')

def getScholarships(parser, schema):
    return parser.select(schema['discriminator'])

def scrap(schema):
    html = getHtml(schema['url'])
    parser = getParser(html)
    for tree in getScholarships(parser, schema):
        scholarshipParser = ScholarshipParser(tree, schema)
        print(scholarshipParser.parse())

cursosEnColombia = {
    'url': 'http://www.curso-en-colombia.com.co/cursos',
    'discriminator': 'div.cursoDItem',
    'title': 'a.cursoDTitCurso',
    'description' : 'div.cursoDDesc',
    'img':'div > img',
}

scrap(cursosEnColombia)
