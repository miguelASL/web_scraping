from bs4 import BeautifulSoup
import pandas as pd
import requests # Con esta librería podemos hacer peticiones a una página web

year = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]
def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup' # Página web de la que queremos obtener la información
    respuesta = requests.get(web) # Hacemos una petición a la página web
    contenido = respuesta.text # Obtenemos el contenido de la página web
    soup = BeautifulSoup(contenido, 'lxml')

    partidos = soup.find_all('div', class_='footballbox') # Buscamos todas las tablas con la clase 'wikitable'

    home = []
    score = []
    away = []
    
    for partido in partidos:
        home.append(partido.find('th', class_='fhome')) 
        score.append(partido.find('th', class_='fscore'))
        away.append(partido.find('th', class_='faway')) 
        
    dict_footbal = {'Home': home, 'Score': score, 'Away': away}
    df = pd.DataFrame(dict_footbal)
    df['Year'] = year
    return df

fifa = [(get_matches(year) for year in year)]

df_fifa=pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa.csv', index=False)


print(get_matches(1982))
