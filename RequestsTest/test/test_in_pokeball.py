import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': 'b99913f43581f1e54cf07a796a516963'
}

def test_status_code():
    response = requests.get(url =f'{URL}/trainers', params = {"level" : 1})
    assert response.status_code == 200

def test_my_trainer_id():
    response = requests.get(url =f'{URL}/trainers', params = {"trainer_id" : 237})
    assert response.json()['data'][0]['trainer_name'] == 'Puma'