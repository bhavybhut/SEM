from evaluate import *
import random, requests, json

def setup_module(module):
    print("\nsetup_module\n")
    """ setup any state specific to the execution of the given module."""

def teardown_module(module):
    print("\nteardown_module\n")
    """ teardown any state that was previously setup with a setup_module
    method.
    """

def test_parse_integer():
    print("\ntest_parse_integer\n")
    for i in range(0,1000):
        s = str(i)
        assert parse_integer(s) == i
    assert parse_integer(8347128311) == 8347128311

def test_parse_integer2():
    print("\ntest_parse_integer2\n")
    for i in range(0,1000):
        s = str(i)
        assert parse_integer(s) == i

def test_parse_float():
    print("\ntest_parse_float\n")
    for _ in range(0,100):
        x = random.uniform(3.3,68.9)
        s = str(x)
        assert parse_float(s) == x

def test_evaluate_height():
    assert evaluate_height(130)
    assert evaluate_height(142)
    assert evaluate_height(155)
    assert evaluate_height(169)
    assert evaluate_height(208)
    assert evaluate_height(231)
    assert evaluate_height(278)

def test_evaluate_phone():
    assert evaluate_phone(3303303300) == 3303303300
    assert evaluate_phone(7736736732) == 7736736732
    assert evaluate_phone(3306785643) == 3306785643

def test_evaluate_coordinates():
    response = requests.get("https://www.metaweather.com/api/location/search/?query=london")
    assert response
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    result = json.loads(response.text)
    assert type(result) is list
    assert len(result) == 1
    data = result[0]
    assert type(data) is dict
    coord = str(data['latt_long']).split(',',2)
    assert evaluate_latitude(coord[0])
    assert evaluate_longitude(coord[1])
    