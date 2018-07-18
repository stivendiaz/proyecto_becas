from requests import get
from bs4 import BeautifulSoup as soup

class ScholarshipParser:
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

def getScholarships(parser, schema):
    return parser.select(schema['discriminator'])

def scrap(schema):
    html = getHtml(schema['url'])
    parser = getParser(html)
    for tree in getScholarships(parser, schema):
        scholarshipParser = ScholarshipParser(tree, schema)
        print(scholarshipParser.parse())

cursosEnColombia = {
    'url': 'https://www.curso-en-colombia.com.co/postgrado',
    'discriminator': 'div.cursoDItem',
    'title': 'a.cursoDTitCurso',
    'description' : 'div.cursoDDesc',
    'img':'div > img',
    'mas_info':'div.largeCentro > a',
    'additional':{
    'url': 'https://www.curso-en-colombia.com.co/postgrado',
    'discriminator': 'div.cursoDItem'}
}

masoportunidades = {
    'url': 'http://masoportunidades.org/category/becas/page/2/',
    'discriminator': 'article.post',
    'title': 'h2.entry-title > a',
    'description' : 'div.entry-content > p',
    'img':'a > img',
    'mas_info' : 'h2.entry-title > a'
}

scrap(masoportunidades)
