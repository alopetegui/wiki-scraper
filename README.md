# wiki-scraper
## Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la wikipedia ["actrices españolas"](https://es.wikipedia.org/wiki/Categor%C3%ADa:Actrices_de_Espa%C3%B1a) e información básica de cada actriz de la lista.
Este script también es válido para otras categorías de la wikipedia con una estructura similar.


## Descripcción ficheros

**pdf/informe.pdf:** Respuestas a las preguntas de la práctica

**src/wiki-scraper.py:** Script de python para hacer web scraping a páginas de categorías de la wikipedia


## Detalles del script
Para ejecutar el script es necesario instalar la siguientes bibliotecas:
```
pip install requests
pip install beautifulsoup4
```

Uso:
```
usage: python3 wiki-scraper.py [-h] [-w WIKI] [-l LIMIT]

optional arguments:
  -h, --help              show this help message and exit
  -w WIKI, --wiki WIKI    url of the wiki category page
  -l LIMIT, --limit LIMIT maximum number of actresses to scrape
```


## DOI Zenodo del dataset

Enlace al dataset: https://doi.org/10.5281/zenodo.5644309


## Miembros del equipo
La actividad ha sido realizada de manera individual por **Ander Lopetegui Arregui**


## Recursos
- Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
- Masip, D. (2010). El lenguaje Python. Editorial UOC.
- Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
