import requests, json

def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_animals():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response
    assert response.status_code == 200
    print(response.headers['Content-Type'])
    assert response.headers['Content-Type'] == 'application/json'
    result = json.loads(response.text)
    assert type(result) is dict
    assert len(result) == 2
    print(result['message'])

def test_books():
    response = requests.get("https://www.booknomads.com/api/v0/isbn/9789000035526")
    assert response
    assert response.status_code == 200
    print(response.headers['Content-Type'])
    assert response.headers['Content-Type'] == 'application.json'
    result = json.loads(response.text)
    assert type(result) is dict
    assert len(result) == 8
    print(result['ISBN'])
    assert result['ISBN'] == '9789000035526'

def test_business():
    response = requests.get("https://api.domainsdb.info/search?query=facebook&tld=com")
    assert response
    assert response.status_code == 200
    print(response.headers['Content-Type'])
    assert response.headers['Content-Type'] == 'application/json'
    result = json.loads(response.text)
    assert type(result) is dict
    assert len(result) == 3
    assert len(result['domains']) == 50

def test_crypto():
    response = requests.get("https://coinbin.org/btc")
    assert response
    assert response.status_code == 200
    print(response.headers['Content-Type'])
    assert response.headers['Content-Type'] == 'application/json'
    result = json.loads(response.text)
    assert type(result) is dict
    assert len(result) == 1
    print(result['coin']['name'])
    assert result['coin']['name'] == 'Bitcoin'
    print("price $" + str(result['coin']['usd']))

def test_science():
    response = requests.get("https://api.spacexdata.com/v2/launches/latest?pretty")
    assert response
    assert response.status_code == 200
    print(response.headers['Content-Type'])
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    result = json.loads(response.text)
    assert type(result) is dict
    assert len(result) == 12
    print(result['rocket']['rocket_name'])
    assert result['rocket']['rocket_name'] == 'Falcon 9'
