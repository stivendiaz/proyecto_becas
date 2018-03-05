from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.curso-en-colombia.com.co/cursos'
#openin up connection
uClient= uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html,"html.parser")

 #information each schoolarship
containers = page_soup.findAll("div",{"class":"cursoDItem"})

#creamos el archivo json

filename = "becas.txt"
f = open(filename, "w")
i=0
for container in containers:
    title = container.div.img["alt"]
    image = container.div.img["src"]

    info = page_soup.findAll("div",{"class":"cursoDInfo"})
    links = info[i].div.findAll('a')
    link_info = links[0]["href"]
    cent_edu = links[1]["title"]

    f.write("titulo: "+ title + "\n" + "imagen: " + image + "\n" + "link info: " + link_info + "\n" + "centro: "+cent_edu+ "\n"+ "\n")


    i+=1
    
f.close()


