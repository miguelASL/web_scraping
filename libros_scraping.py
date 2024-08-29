import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de una página de práctica
url = 'http://books.toscrape.com/'

# Configurar los encabezados para simular un navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

# Realizar la solicitud HTTP para obtener el HTML de la página
response = requests.get(url, headers=headers)

# Comprobar que la solicitud fue exitosa
if response.status_code == 200:
    html = response.text

    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar los contenedores de libros
    books = soup.find_all('article', class_='product_pod')

    # Crear listas vacías para almacenar los datos
    data = {
        "Título": [],
        "Precio": [],
        "Disponibilidad": []
    }

    # Iterar sobre cada contenedor de libro para extraer datos
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()

        # Guardar los datos en las listas correspondientes
        data['Título'].append(title)
        data['Precio'].append(price)
        data['Disponibilidad'].append(availability)

    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(data)

    # Mostrar el DataFrame
    print(df)
else:
    print(f'Error al obtener la página: {response.status_code}')
