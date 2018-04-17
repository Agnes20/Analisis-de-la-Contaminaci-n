# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import simplejson as json
import codecs # para el poder utilizar el encoding='utf-8', para el python 2.7.XX#
from pygeocoder import Geocoder #Libreria para sacar las coordenadas de una dirección que le pasas
import time # tiempo
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
#SIEMPRE TABULAR EN PYTHON, SINO NO FUNCIONA
root_url = "https://www.idealista.com"
print("¿Cómo se la fichero .json?")
#poner ' ' en los lados del nombre del fichero
fichero = input()
with open(fichero, 'r') as f:
    distros_dict = json.load(f)
    f = codecs.open('datos_openrefine.json', mode='w', encoding='utf-8') #se necesita el codecs para poder hacer el archivo,para el python 2.7.XX##
    idealista_houses = list()
for distro in distros_dict:
    active_url = distro['url']
    #anuncio = distro['name']
    descripcion = distro['description']
    req  = requests.get(root_url+active_url)
    data = req.text
    soup = BeautifulSoup(data, "html.parser")
    houses = soup.find_all("div", class_="clearfix ide-container ide-container-detail")
    # OTRA OPCION: houses = soup_find_all('element', {'class': ""})
    #Error "TypeError: Object of type Tag is not JSON serializable" es una variable que no es formato texto sin html, pasar a texto
    for house in houses:
        name = house.find("span", class_="main-info__title-main").text
        street2 = house.find("span", class_="main-info__title-minor")
        street = street2.text
        alquiler2 = house.find("div", class_="info-data")
        alquiler = alquiler2.text
        #descripcion2 = house.find("div", class_="comment")
        ubicacion2 = house.find("div", id="headerMap")
        ubicacion = ubicacion2.text
        idealista_houses.append({
            'name': name,
            'street' : street,
            'alquiler': alquiler,
            'descripcion': descripcion,
            'ubicacion': ubicacion,
        })
        #tiene que ser todo texto sino no lo guarda en .json
    resultado = json.dumps(idealista_houses, indent=4, ensure_ascii=False, encoding="utf-8")
finalizado = "Terminado"
print(finalizado)
f.write(resultado)      
f.close()