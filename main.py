import time
import pywhatkit as pwk
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import locale
from click import core
from requests import Response
import pyautogui, webbrowser
from time import sleep
import keyboard as k

#locale.setlocale(locale.LC_ALL, 'es-ES')





noti1 = ""
noti2 = ""
noti3 = ""
noti4 = ""
noti5 = ""
noti6 = ""
noti7 = ""
noti8 = ""
noti9 = ""
noti10 = ""
noti11 = ""
noti12 = ""
noti13= ""
noti14 = ""
noti15 = ""
noti16 = ""
noti17 = ""
noti18 = ""
noti19 = ""
noti20 = ""
noti21 = ""
noti22 = ""
noti23 = ""
noti24 = ""
noti25 = ""
noti26 = ""
noti27 = ""
noti28 = ""
noti29 = ""
noti30 = ""

width,height = pyautogui.size()
countwp = 0
noti = ["0","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) "
        ,"1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) "
        ,"1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) "
        ,"1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) "
        ,"1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) "
        ,"1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) ","1) ","2) ","3) ","4) ","5) "]




#pywhatkit.sendwhatmsg("+573043840402",texto,13,12)
#pwk.sendwhatmsg_instantly("+573043840402",texto)


#pyautogui.click(width/2,height/2)
#pyautogui.press("enter")
#webbrowser.open('https://web.whatsapp.com/send?phone=573043840402')
#sleep(15)
#pyautogui.typewrite(texto)





#WebScrapping  a 9 links

descrip = list()
links = list()
titulos = list()
comunidades = list()


#Comunidad Emprendedores
url = 'https://www.emprendedores.es/seccion/guia-juridica-fiscal/page/'
url2 = 'https://www.emprendedores.es/seccion/casos-de-exito/page/'
url3 = 'https://www.eleconomista.es/pymes/'



for page in range(1, 6):

    if page < 3:
        req = requests.get(url + str(page) + '/')
        soup = BeautifulSoup(req.text, 'html.parser')
    else:
        req = requests.get(url2 + str(page) + '/')
        soup = BeautifulSoup(req.text, 'html.parser')

    # titulo

    titulo = soup.find_all('h2', class_='full-item-title item-title entry-title')
    for i in titulo:
        titulos.append(i.text.rstrip().replace('\n', ""))
        comunidades.append("Emprendedores")

    # Descripcion

    des = soup.find_all('div', class_='full-item-dek item-dek')
    for i in des:
        descrip.append(i.text.lstrip().replace('\n', ""))


    # links
    head_links = soup.findAll('h2', {'class': 'full-item-title item-title entry-title'})
    for n in head_links:
        for a in n.find_all('a', href=True):
            links.append(a['href'])


page = requests.get(url3)
soup = BeautifulSoup(page.content, 'html.parser')

# titulo
titulo = soup.find_all('h2', class_='h3')
count = 0
for i in titulo:
    if count > 0:
        titulos.append(i.text.rstrip().replace('\n', ""))
        comunidades.append("Emprendedores")
        #print(i.text.rstrip().replace('\n', ""))
    count = count + 1



# Descripcion
des = soup.find_all('p', class_='articleText')
for i in des:
    descrip.append(i.text.lstrip().replace('\n', ""))


# links
count1 = 0
head_links = soup.findAll('h2', {'class': 'h3'})
for n in head_links:
    for a in n.find_all('a', href=True):
        if count1 > 0:
            links.append(a['href'].replace('//',""))
            #print(a['href'])
    count1 = count1 + 1


#Comunidad Empresa y discapacidad


url4 = 'https://blogs.iadb.org/ideas-que-cuentan/es/page/'
url5 = 'https://blogs.iadb.org/conocimiento-abierto/es/page/'

for page in range(1, 9):

    if page < 5:
        req = requests.get(url4 + str(page) + '/')
        soup = BeautifulSoup(req.text, 'html.parser')
    else:
        req = requests.get(url5 + str(page) + '/')
        soup = BeautifulSoup(req.text, 'html.parser')

    # titulo
    titulo = soup.find_all('h2', class_='entry-title')

    for i in titulo:
        titulos.append(i.text.rstrip().replace('\n', ""))
        comunidades.append("Empresa y discapacidad")
    # print(i.text.rstrip().replace('\n', ""))

    # Descripcion
    des = soup.find_all('div', class_='entry-content')
    for i in des:
        descrip.append(i.text.lstrip().replace('\n', ""))
        #print(i.text.lstrip().replace('\n', ""))

    # links

    head_links = soup.findAll('h2', {'class': 'entry-title'})
    for n in head_links:
        for a in n.find_all('a', href=True):
            links.append(a['href'])
            #print(a['href'])




url6 = 'http://iberinclusion.org/catalogo-de-buenas-practicas'
page = requests.get(url6)
soup = BeautifulSoup(page.content, 'html.parser')

# titulo
titulo = soup.find_all('div', class_='views-field views-field-title')

for i in titulo:
    titulos.append(i.text.rstrip().replace('\n', ""))
    comunidades.append("Empresa y discapacidad")
    #print(i.text.sp)



# Descripcion
des = soup.find_all('div', class_='views-field views-field-field-breve-descripci-n-')
for i in des:
    descrip.append(i.text.lstrip().replace('\n', ""))
    #print(i.text.lstrip().replace('\n', ""))


# links

head_links = soup.findAll('div', {'class': 'views-field views-field-title'})
for n in head_links:
    for a in n.find_all('a', href=True):
         links.append('http://iberinclusion.org/'+a['href'])
         #print('http://iberinclusion.org/'+a['href'])



#Comunidad Mipymes


url7 = 'https://recruitingdaily.com/articles/page/'
page = requests.get(url7)
soup = BeautifulSoup(page.content, 'html.parser')

for page in range(1, 3):
    req = requests.get(url7 + str(page)+ '/')
    soup = BeautifulSoup(req.text, 'html.parser')
    # titulo
    titulo = soup.find_all('h4', class_='card-title')

    for i in titulo:
        titulos.append(i.text.rstrip().replace('\n', ""))
        comunidades.append("Mipymes")
        # print(i.text)

    # Descripcion
    des = soup.find_all('div', class_='col-lg-4 col-md-12 order-lg-2 card-content')
    for i in des:
        descrip.append(i.text.lstrip().replace('\n', ""))
        # print(i.text.lstrip().replace('\n', ""))

    # links

    head_links = soup.findAll('h4', {'class': 'card-title'})
    for n in head_links:
        for a in n.find_all('a', href=True):
            links.append(a['href'])
            # print('http://iberinclusion.org/'+a['href'])



url8 = 'https://www.humans4health.es/actualidad?page='
page = requests.get(url8)
soup = BeautifulSoup(page.content, 'html.parser')

for page in range(1, 3):

    req = requests.get(url8 + str(page))
    soup = BeautifulSoup(req.text, 'html.parser')
    # titulo
    titulo = soup.find_all('div', class_='title')

    count3 = 0
    for i in titulo:
        if count3 > 0:
            titulos.append(i.text.rstrip().replace('\n', ""))
            comunidades.append("Mipymes")
            # print(i.text.rstrip().replace('\n', ""))
        count3 = count3 + 1

    # Descripcion
    des = soup.find_all('div', class_='subtitle')
    for i in des:
        descrip.append(i.text.lstrip().replace('\n', ""))
        # print(i.text.lstrip().replace('\n', ""))

    # links
    head_links = soup.findAll('div', {'class': 'title'})
    for n in head_links:
        for a in n.find_all('a', href=True):
            links.append('https://www.humans4health.es' + a['href'])
            # print('http://iberinclusion.org/'+a['href'])


url9 = 'https://www.portafolio.co/innovacion'
page = requests.get(url9)
soup = BeautifulSoup(page.content, 'html.parser')


# titulo
titulo = soup.find_all('h3', class_='listing-title')

count4 = 0
for i in titulo:
    if count4 < 15:
        titulos.append(i.text.rstrip().replace('\n', ""))
        comunidades.append("Mipymes")
        #print(i.text.rstrip().replace('\n', ""))
    count4 = count4 + 1



# Descripcion
des = soup.find_all('p', class_='listing-epigraph')
for i in des:
    descrip.append(i.text)
    #print(i.text)

des = soup.find_all('div', class_='listing-epigraph')
for i in des:
    descrip.append(i.text)
    #print(i.text)


# links
count5 = 0
head_links = soup.findAll('h3', {'class': 'listing-title'})
for n in head_links:
    for a in n.find_all('a', href=True):
        if count5 < 15:
            links.append('https://www.portafolio.co'+a['href'])
         #print('http://iberinclusion.org/'+a['href'])
        count5 = count5 + 1


df1 = pd.DataFrame({'Comunidades':comunidades,'titulo': titulos,'Descripcion': descrip,'links':links})
df = pd.DataFrame({'titulo': titulos,'links':links})
#print(df1)

df1.to_excel("comunidades.xlsx")

df.to_csv('links.csv',index=False)


with open("links.csv","r",encoding="utf8") as file:
    for line in file:
        if countwp > 0 and countwp < 6:
          noti1 = noti1 + noti[countwp] + line
        if countwp > 5 and countwp < 11:
          noti2 = noti2 + noti[countwp] + line
        if countwp > 10 and countwp < 16:
          noti3 = noti3 + noti[countwp] + line
        if countwp > 15 and countwp < 21:
            noti4 = noti4 + noti[countwp] + line
        if countwp > 20 and countwp < 26:
            noti5 = noti5 + noti[countwp] + line
        if countwp > 25 and countwp < 31:
            noti6 = noti6 + noti[countwp] + line
        if countwp > 30 and countwp < 36:
            noti7 = noti7 + noti[countwp] + line
        if countwp > 35 and countwp < 41:
            noti8 = noti8 + noti[countwp] + line
        if countwp > 40 and countwp < 46:
            noti9 = noti9 + noti[countwp] + line
        if countwp > 45 and countwp < 51:
            noti10 = noti10 + noti[countwp] + line
        if countwp > 50 and countwp < 56:
            noti11 = noti11 + noti[countwp] + line
        if countwp > 55 and countwp < 61:
            noti12 = noti12 + noti[countwp] + line
        if countwp > 60 and countwp < 66:
            noti13 = noti13 + noti[countwp] + line
        if countwp > 65 and countwp < 71:
            noti14 = noti14 + noti[countwp] + line
        if countwp > 70 and countwp < 76:
            noti15 = noti15 + noti[countwp] + line
        if countwp > 75 and countwp < 81:
            noti16 = noti16 + noti[countwp] + line
        if countwp > 80 and countwp < 86:
            noti17 = noti17 + noti[countwp] + line
        if countwp > 85 and countwp < 91:
            noti18 = noti18 + noti[countwp] + line
        if countwp > 90 and countwp < 96:
            noti19 = noti19 + noti[countwp] + line
        if countwp > 95 and countwp < 101:
            noti20 = noti20 + noti[countwp] + line
        if countwp > 100 and countwp < 106:
            noti21 = noti21 + noti[countwp] + line
        if countwp > 105 and countwp < 111:
            noti22 = noti22 + noti[countwp] + line
        if countwp > 110 and countwp < 116:
            noti23 = noti23 + noti[countwp] + line
        if countwp > 115 and countwp < 121:
            noti24 = noti24 + noti[countwp] + line
        if countwp > 120 and countwp < 126:
            noti25 = noti25 + noti[countwp] + line
        if countwp > 125 and countwp < 131:
            noti26 = noti26 + noti[countwp] + line
        if countwp > 130 and countwp < 136:
            noti27 = noti27 + noti[countwp] + line
        if countwp > 135 and countwp < 141:
            noti28 = noti28 + noti[countwp] + line
        if countwp > 140 and countwp < 146:
            noti29 = noti29 + noti[countwp] + line
        if countwp > 145 and countwp < 151:
            noti30 = noti30 + noti[countwp] + line
        countwp = countwp + 1



str = "Hola neni espero tengan un excelente dia Encuentra los articulos mas importantes para hoy "
dias = [str + "viernes 23 Abril 2022" + '\n' + '\n' + noti1,str+ "Sabado 24 Abril 2022" + '\n' + '\n' + noti2,str + "Domingo 25 Abril 2022"+ '\n' + '\n' + noti3,
        str+ "Lunes 26 Abril 2022" + '\n' + '\n' + noti4,str+ "Martes 27 Abril 2022" + '\n' + '\n' + noti5,str+ "Miercoles 28 Abril 2022" + '\n' + '\n' + noti6,
        str+ "Jueves 29 Abril 2022" + '\n' + '\n' + noti7,str+ "viernes 30 Abril 2022" + '\n' + '\n' + noti8,str+ "Sabado 01 Mayo 2022" + '\n' + '\n' + noti9,
        str+ "Domingo 02 Mayo 2022" + '\n' + '\n' + noti10,str+ "Lunes 03 Mayo 2022" + '\n' + '\n' + noti11,str+ "Martes 04 Mayo 2022" + '\n' + '\n' + noti12,
        str+ "Miercoles 05 Mayo 2022" + '\n' + '\n' + noti13,str+ "Jueves 06 Mayo 2022" + '\n' + '\n' + noti14,str+ "viernes 07 Mayo 2022" + '\n' + '\n' + noti15,
        str+ "Sabado 08 Mayo 2022" + '\n' + '\n' + noti16,str+ "Domingo 09 Mayo 2022" + '\n' + '\n' + noti17,str+ "Lunes 10 Mayo 2022" + '\n' + '\n' + noti18,
        str+ "Martes 11 Mayo 2022" + '\n' + '\n' + noti19,str+ "Miercoles 12 Mayo 2022" + '\n' + '\n' + noti20,str+ "Jueves 13 Mayo 2022" + '\n' + '\n' + noti21,
        str+ "viernes 14 Mayo 2022" + '\n' + '\n' + noti22,str+ "Sabado 15 Mayo 2022" + '\n' + '\n' + noti23,str+ "Domingo 16 Mayo 2022" + '\n' + '\n' + noti24,
        str+ "Lunes 17 Mayo 2022" + '\n' + '\n' + noti25,str+ "Martes 18 Mayo 2022" + '\n' + '\n' + noti26,str+ "Miercoles 19 Mayo 2022" + '\n' + '\n' + noti27,
        str+ "Jueves 20 Mayo 2022" + '\n' + '\n' + noti28,str+ "viernes 21 Mayo 2022" + '\n' + '\n' + noti29,str+ "Sabado 22 Mayo 2022" + '\n' + '\n' + noti30]

countdias = 0
while True:
    time.sleep(10) #86400 seconds in a day
    pwk.sendwhatmsg_instantly("+573043840402",dias[countdias])
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    k.press_and_release('enter')
    countdias = countdias + 1    


