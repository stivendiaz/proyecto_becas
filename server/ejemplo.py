from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#openin up connection
uClient= uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html,"html.parser")
 #grabs each product
container = page_soup.findAll("div",{"class":"item-container"})

filename = "productos.csv"
f = open(filename, "w")

headers  ="brand, product_name, shipping \n"

f.write(headers)


for containr in container:

    brand = containr.div.div.a.img["title"]

    title_container = containr.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text


    shipping_container = containr.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: "+ product_name)
    print("shipping: "+shipping)
    f.write(brand + ","+product_name.replace(",","|") + ","+shipping + "\n")
f.close()
