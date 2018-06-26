from requests import get
from bs4 import BeautifulSoup as soup

class ScholarshipParser:
    def __init__(self, tree, schema):
        self.tree = tree
        self.schema = schema

    def parse(self):
        return { 'title': self.getTitle() }

    def getTitle(self):
        title = self.tree.find('a', { 'class': self.schema['title'] })
        return title.string

def getHtml(url):
    response = get(url)
    return response.text

def getParser(html):
    return soup(html, 'html.parser')

def getScholarships(parser, schema):
    return parser.findAll('div', { 'class': schema['discriminator'] })

def scrap(schema):
    html = getHtml(schema['url'])
    parser = getParser(html)
    for tree in getScholarships(parser, schema):
        scholarshipParser = ScholarshipParser(tree, schema)
        print(scholarshipParser.parse())

cursosEnColombia = {
    'url': 'http://www.curso-en-colombia.com.co/cursos',
    'discriminator': 'cursoDItem',
    'title': 'cursoDTitCurso'
}

scrap(cursosEnColombia)
