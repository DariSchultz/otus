import requests
import pytest


def test_get_all_breeds():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    assert response.status_code == 200

def test_get_random_image():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200

@pytest.mark.parametrize('quantity', ['1', '5', '10', '100'])
def test_get_image_random_breed_by_qantity(quantity):
    response = requests.get(f'https://dog.ceo/api/breed/hound/images/random/{quantity}')
    print(response.status_code)
    assert response.status_code == 200

@pytest.mark.parametrize('breed', ['pug', 'akita', 'borzoi', 'eskimo', 'pitbull'])
def test_get_image_by_specific_breed(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images')
    print(response.status_code)
    assert response.status_code == 200

@pytest.mark.parametrize('subbreed', ['afghan', 'blood', 'english'])
def test_get_image_by_specific_subbreed(subbreed):
    response = requests.get(f'https://dog.ceo/api/breed/hound/{subbreed}/images')
    assert response.status_code == 200