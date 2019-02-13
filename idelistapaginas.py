# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import simplejson as json
import codecs # para el poder utilizar el encoding='utf-8', para el python 2.7.XX#
'''
La documentacion puede ser encontrada en
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''

## Helper functions
def get_data_safely(list_, index, default):
    try:
        return list_[index].text
    except IndexError:
        return default

def parse(text):
    return bytes(text, 'utf-8').decode('utf-8', 'strict')



## Codigo de la mision
print("¿Cómo se llama la url?")
#poner las " " en los lados de la url
active_url = input()
root_url = "https://www.idealista.com"
idealista_houses = list()
while True:
    req  = requests.get(root_url+active_url)
    data = req.text
    soup = BeautifulSoup(data, "html.parser")
    houses = soup.find_all("div", class_="item")
    # OTRA OPCION: houses = soup_find_all('element', {'class': ""})
    #Error "TypeError: Object of type Tag is not JSON serializable" es una variable que no es formato texto sin html, pasar a texto
    for house in houses:
        item_link = house.find("a", class_="item-link")
        name = item_link.text
        price = house.find("span", class_="item-price").text
        details = house.find_all("span", class_="item-detail")
        rooms = get_data_safely(details, 0, "")
        size = get_data_safely(details, 1, "")
        moreinfo = get_data_safely(details, 2, "")
        url = item_link['href']
        descriptions = house.find("div", class_="item-description description")
        if descriptions==None:
            texto = "No hay descripcion"
            description = texto
        else:
            description = descriptions.text
        #poner en un pack 
        idealista_houses.append({
            'name': name,
            'url': url,
            'price': price,
            'rooms': rooms,
            'size': size,
            'moreinfo': moreinfo,
            'description': description,
        })
    next_url = soup.find("a", class_="icon-arrow-right-after")
    if not next_url:
        break
    active_url = next_url["href"]

#print(json.dumps(idealista_houses, indent=4, ensure_ascii=False, encoding="utf-8"))

resultado = json.dumps(idealista_houses, indent=4, ensure_ascii=False, encoding="utf-8")
finalizado = "Terminado"
print(finalizado)
f = codecs.open('lista_anuncios.json', mode='w', encoding='utf-8') #se necesita el codecs para poder hacer el archivo,para el python 2.7.XX##
f.write(resultado)
f.close()
