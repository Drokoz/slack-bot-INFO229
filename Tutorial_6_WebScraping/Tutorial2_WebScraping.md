# Web scraping con Python

Web scraping es un método de automatización para extraer información de páginas web. esto tiene distintas funcionalidades como:

 - Comparación de precios
 - Obtener información de páginas de redes sociales para perfilamiento
 - Investigaciones y desarrollo
 - Entre otras

## ¿Por qué Python?

Python es un lenguaje de programación con una sintaxis muy simple, además tiene una gran colección de librerías con un buen apoyo para web scraping (NumPy, Matplotlib, Pandas, etc).

## ¿Cómo hacer web scraping?

Primero hay que entender cómo funciona. Cuando uno hace web scraping al ejecutar un código se debe mandar una consulta a un URL (dirección de la página web a la cual se quiere obtener la información). Como respuesta a esa consulta el servidor envía la información que permite ser leída mediante páginas HTML o XML, por lo que con código python se puede extraer lo "importante" de estas páginas.

Para extraer información usando web scraping se deben seguir los siguientes pasos:

 1. Encontrar la dirección URL de la página a la cual se quiere extraer información.
 2. Usar la herramienta de "inspeccionar" en el navegador web.
 3. Encontrar el dónde está la información que se quiere obtener.
 4. Escribir un código que te permita obtener la información.
 5. Guardar la información.

# Ejemplo de web scraping

## Primero, vamos a definir distintas librerías que serán usadas en el ejemplo.

 - **Selenium:** Selenium es una librería de testing para web. Se usa para automatizar actividades de un navegador web.
 - **BeautifulSoup:** BeautifulSoup es una librería que convertir las respuestas HTML o XML en data legible y más fácil de extraer.
 - **Pandas:** Pandas es una librería para la manipulación de data, generalmente se usa para el análisis de esta mediante tablas y estadística. Es usada para extraer la información y guardarla en el formato deseado.

## Segundo, los pre-requisitos.

 - Python 3.x con las librerías mencionadas anteriormente instaladas.
 - Navegador web Google Chrome.
 - Sistema operativo Ubuntu.

## Tercera, los pasos.

 ### 1. Encontrar el URL que se quiere obtener información.
En este caso usaremos SoloTodo una página de venta el cual buscaremos el precio y nombre  de computadores.
### 2. Inspeccionar la página.
![inspeccionar](https://github.com/Drokoz/slack-bot-INFO229/blob/master/Tutorial_6_WebScraping/tutorial2-imagenes/inspeccionar.png) 
### 3. Encontrar la data inspeccionando los elementos que queremos obtener.
![selec](https://github.com/Drokoz/slack-bot-INFO229/blob/master/Tutorial_6_WebScraping/tutorial2-imagenes/selec.png) 
![selec1](https://github.com/Drokoz/slack-bot-INFO229/blob/master/Tutorial_6_WebScraping/tutorial2-imagenes/selec2.png) 
![selec2](https://github.com/Drokoz/slack-bot-INFO229/blob/master/Tutorial_6_WebScraping/tutorial2-imagenes/selec3.png) 
![selec3](https://github.com/Drokoz/slack-bot-INFO229/blob/master/Tutorial_6_WebScraping/tutorial2-imagenes/selec4.png) 
### 4. Escribir el código.
Primero se deberá crear el archivo Python, esto se puede hacer de varias maneras, pero se usará el siguiente comando en la carpeta que desea realizar su proyecto.
En este caso llamaremos al archivo "ws_soloTodo"
~~~
gedit ws_soloTodo.py
~~~
Ahora con el archivo abierto partiremos importando las librerias necesarias.
~~~
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
~~~
Para configurar nuestro driver (forma automatizada para navegar en la web) que se usará para la extracción de datos tendremos que usar el siguiente comando, así se usará el navegador Google Chrome.
~~~
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
~~~
Ahora declaramos las listas que almacenaran nuestra información.
~~~
product= [] #Lista para los nombres
precios= [] #Lista para los precios
~~~
Consulta del driver a donde queremos sacar la información.
~~~
driver.get("https://www.solotodo.cl/notebooks")
~~~
Ahora el código principal.
~~~
#Obtener el contenido de la pagina
content = driver.page_source 
#Transformar la consulta a ua forma legible
soup = BeautifulSoup(content)
#Iterar en todo lo encontrado e ir extrayendo lo necesario solamente
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	name=a.find('div', attrs={'class':'_3wU53n'})
	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	product.append(name.text)
	prices.append(price.text)
~~~
### 5. Ejecutar el código en el terminal con el siguiente comando.
~~~
python3 wb_soloTodo.py
~~~
Una vez estemos listos y que funcione podremos agregar al código lo siguiente.
~~~
df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
~~~
Esto almacenará lo obtenido en un "data frame" de pandas para luego ser convertido a un archivo csv (tipo 'excel')

## Documentación
- [1](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
- [2](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/web-scraping-con-python/)
- [3](https://selenium-python.readthedocs.io/)
- [4](https://pandas.pydata.org/#:~:text=pandas%20is%20a%20fast%2C%20powerful,of%20the%20Python%20programming%20language.)
- [5](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
