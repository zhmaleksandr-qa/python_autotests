import requests

URL = 'https://api.pokemonbattle.me/v2'

HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': 'b99913f43581f1e54cf07a796a516963'
}

# создание покемона

body = {
    "name": "Mimino",
    "photo": "https://dolnikov.ru/pokemons/albums/027.png"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)

# Изменение имени покемона

body_name = {
    "pokemon_id": response.json()['id'],
    "name": "Tamagawk",
    "photo": "https://dolnikov.ru/pokemons/albums/056.png"
}

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_name)
print(response_name.text)

# Добавление покемона в покебол

body_pokeball = {
    "pokemon_id": response_name.json()['id']
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokeball)
print(response_pokeball.text)
