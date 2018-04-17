1. Título
  - Análisis de la Contaminación
2. Introducción. 
 -Objetivo del proyecto
  - El objetivo del proyecto es poder ver en un mapa, la dispersión del polen por valencia, a su vez tener los datos de los     alquileres por toda valencia. Para poder saber si eres alérgico, saber por que zonas puedes vivir con mas probabilidad de tener más alergia o no. También tenemos los puntos que tiene la cuidad de valencia con los datos de contaminación del aire si buena por esa zona o no.
 -El problema a resolver
  - Recogida de los datos de los pisos.
    - WebScrapping con Python, BeutifulShoup y OpenRefine.
  - Recogida de los datos del polen.
    - Web Portal de Transparencia de Valencia, QGIS 3 y OpenRefine.
  -Recogida de los datos de la contaminación.
   - Web Portal de Transparencia de Valencia, My Google Maps y OpenRefine.
3. Descripción de la solución planteada.
  - Recogida de los datos de los pisos.
    - Mediante el WebScrapping con Python y BeutifulShoup, creamos los Códigos idelistapaginas.py y idelistapaginasmapa.py.
     - El Código idelistapaginas.py obtenemos los datos generales de los pisos y solo le pasamos el link que quieres explorar.
     - El Código idelistapaginasmapa.py obtenemos los datos que nos faltan de los pisos con más profundidad y solo le pasamos el nombre del archivo .JSON (creado con el programa idelistapaginas.py) que quieres explorar y actualizamos los datos que nos faltan de los pisos.
     - Obtenemos los datos de los pisos en formato .JSON y con OpenRefine de hace una limpieza a fondo de los datos que deseamos mostrar en el mapa.
  - Recogida de los datos del polen.
    - Obtenemos los de la Web Portal de Transparencia de Valencia y mediante el programa QGIS 3 sacamos los puntos, quitamos los puntos que no nos interesan y le insertamos los que datos que nos interesa y lo guardamos como .GEOJSON
  -Recogida de los datos de la contaminación.
   - Web Portal de Transparencia de Valencia, My Google Maps y OpenRefine.
   - Obtenemos los de la Web Portal de Transparencia de Valencia y mediante el programa My google Maps sacamos las coordenadas de los punto y con el programa OpenRefine le insertamos los que datos que nos interesa y lo guardamos como .CSV o .XLS
4. Metodología.
 - 1. Recogida de los datos de la Webs
 - 2. Limpieza de los datos con los programas QGIS 3, My Google Maps y OpenRefine
 - 3. Utilizamos el programa GIS Cloud para insertar los datos en un Mapa hecho por Capas.
 - 4. Mapa finalizado
5. Resultados.
 - Mapa finalizado: http://editor.giscloud.com/map/854089/mapa-valencia 
6. Guía de uso.
 -  El Código idelistapaginas.py obtenemos los datos generales de los pisos y solo le pasamos el link que quieres explorar.
 -  El Código idelistapaginasmapa.py obtenemos los datos que nos faltan de los pisos con más profundidad y solo le pasamos el nombre del archivo .JSON (creado con el programa idelistapaginas.py) que quieres explorar y actualizamos los datos que nos faltan de los pisos.
 - Los datos que están dentro de la carpeta del polen ya están limpios y modificados a mi gusto por el programa QGIS 3.
7. Términos de uso. 
 - El contenido de este repositorio está sujeto a la licencia GNU General Public License v3.0.
