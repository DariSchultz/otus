import requests
import pytest


def test_get_list_all_breweries():
        response = requests.get('https://api.openbrewerydb.org/v1/breweries')
        assert response.status_code == 200

@pytest.mark.parametrize('country', ['austria', 'ireland'])
def test_get_list_breweries_by_country(country):
        response = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_country={country}')
        assert response.status_code == 200

@pytest.mark.parametrize('city', ['lisboa', 'arundel', 'uckfield', 'porto'])
def test_get_list_breweries_by_city(city):
        response = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_city={city}')
        assert response.status_code == 200
        
@pytest.mark.parametrize('name', ['bushys_brewery_ltd', 'anders_browar'])
def test_get_list_breweries_by_name(name):
        response = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_name={name}')
        assert response.status_code == 200

@pytest.mark.parametrize('type', ['micro', 'regional', 'large', 'contract'])
def test_get_list_breweries_by_type(type):
        response = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_type={type}')
        assert response.status_code == 200