"""
lista los 151 primeros pokemons utilizando la PokeApi
"""
import requests

url="https://pokeapi.co/api/v2/pokemon?limit=151"
response= requests.get(url)
data=response.json()

for pokemon in data["results"]:
    print(pokemon["name"])