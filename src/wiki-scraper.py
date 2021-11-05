import requests
import csv
import re
import time
import argparse
from random import randint
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    */*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "no-cache",
    "dnt": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5\
    37.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w","--wiki", type=str, help="url of the wiki category page")
    parser.add_argument("-l","--limit", type=int, help="maximum number of actresses to scrape")
    parser.set_defaults(wiki='https://es.wikipedia.org/w/index.php?title=Categor%C3%ADa:Actrices_de_Espa%C3%B1a', limit=10000)
    return parser

def scrape_wiki(wiki_page,limit):    
    count=0
    siguiente='true'

    start_time = time.time()
    with open('wiki-scraper.csv', 'w', newline='') as csvfile:
        #Imprimimos cabecera en el csv
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["Nombre","Tiene infobox","Nombre de Nacimiento","Nacimiento","Fallecimiento","link_imagen","link_wiki"])

        #Recorremos todos los links mientras haya una siguiente página
        while siguiente!="" and count<limit:
            page = requests.get(wiki_page,headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")

            #Recorremos todos los links de la lista
            for link in soup.find('div', id = 'mw-pages').find_all('li'):
                link_wiki = ('https://es.wikipedia.org'+(re.search('.*href="(.+?)".*', str(link.a)).group(1)).replace('\n', '')).strip()
                sub_page = requests.get(link_wiki,headers=headers)
                soup_sub_page = BeautifulSoup(sub_page.content, "html.parser")
                nombre=re.search('(.+?) - Wikipedia',soup_sub_page.title.text).group(1).replace('\n', '').strip()   
                print(nombre)        
                try:
                    link_imagen=('https://upload'+(re.search('https://upload(.+?)"',str(soup_sub_page.find_all("meta"))).group(1)).replace('\n', '')).strip()
                except:
                    link_imagen=""
                
                infobox = soup_sub_page.find("table", attrs={"class":"infobox biography vcard"})
                nombre_nacimiento=""
                nacimiento=""
                fallecimiento=""
                tiene_infobox="si"
                try:
                    #Obtenemos los datos del infobox
                    for tr in infobox.tbody.find_all("tr"): # find all tr's from table's 
                        if re.match('Nombre de', tr.text):
                            nombre_nacimiento=tr.find_next().find_next().text.replace('\n', '').strip()
                        if re.match('Nacimiento', tr.text):
                            nacimiento=tr.find_next().find_next().text.replace('\n', '').strip()
                        if re.match('Fallecimiento', tr.text):
                            fallecimiento=tr.find_next().find_next().text.replace('\n', '').strip()
                except:
                    tiene_infobox="no"

                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([nombre,tiene_infobox,nombre_nacimiento,nacimiento,fallecimiento,link_imagen,link_wiki])
                count+=1
                if count == limit:
                    break
                
                #Sleep para evitar ser bloqueado
                time.sleep(randint(0, 3))
            siguiente=soup.find_all('a',text='página siguiente')
            if siguiente:
                wiki_page='https://es.wikipedia.org'+siguiente[0]['href']
            else:
                siguiente=""


def main(args=None):
    parser = get_parser()
    args = parser.parse_args()
    scrape_wiki(args.wiki,args.limit)

if __name__ == '__main__':
    main()

