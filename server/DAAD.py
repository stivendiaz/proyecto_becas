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
    #buscamos el titulo de la beca
    title = container.div.img["alt"]
    #buscamos la imagen de la beca
    image = container.div.img["src"]

    #nos ubicamos en  el div en donde estan los link de informacion y el centro educativo y extraemos los datos
    info = page_soup.findAll("div",{"class":"cursoDInfo"})
    links = info[i].div.findAll('a')
    link_info = links[0]["href"]
    centro_edu = links[1]["title"]

    #nos ubicamos en el mismo div pero buscamos el link de mas informacion
    info_container = info[i].div.findAll('div')
    more_info= info_container[1].a["href"]

    #descripcion
    cont_desc = info[i].findAll('div',{"class":"cursoDDesc fl"})
    descrip = cont_desc[0].text

    #agrupamos por categoria lugar y modalidad
    varios = info[i].findAll('div',{"class":"cursoDParams fl"})
    array = varios[0].findAll('div')

    categoria = array[0].span.a["title"]
    modalidad = array[2].findAll('span')[0].text
    
    lugar=""

    if modalidad == 'Presencial':
        lugar=array[1].span.a["title"]
    


    f.write("titulo: "+ title + "\n" + "imagen: " + image + "\n" + "link info: " + link_info + "\n" + "centro: "+centro_edu+ "\n"+"mas info: "+more_info +"\n"+"categoria: "+categoria+"\n"+"modalidad: "+modalidad+"\n"+"lugar "+lugar+"\n"+"\n")


    i+=1
    
f.close()


