import requests
import pytest


def test_get_getting_all_resources():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200

@pytest.mark.parametrize("id", ['1', '2', '10', '100'])
def test_get_getting_specific_resource_by_id(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
    assert response.status_code == 200

@pytest.mark.parametrize('section, resource', [('posts', 'comments'), ('albums', 'photos'),
                                                 ('users', 'albums'), ('users', 'todos'),
                                                 ('users', 'posts')])
def test_get_listing_nested_resources(section, resource):
    response = requests.get(f'https://jsonplaceholder.typicode.com/{section}/1/{resource}')
    assert response.status_code == 200

@pytest.mark.parametrize('title, body, userId', [('first title', 'first body', 1), ('second title', 'second body', 2),
                                                 ('third title', 'third body', 3), ('fourth title', 'fourth body', 4),
                                                 ('fifth title', 'fifth body', 5)])
def test_get_creating_resource(title, body, userId):
    response = requests.get('https://jsonplaceholder.typicode.com/posts', json ={'title': f'{title}', 'body': f'{body}', 'userId': f'{userId}'})
    assert response.status_code == 200

@pytest.mark.parametrize("id", [1, 2, 3, 4, 5])
def test_updating_resource(id):
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{id}", json={"title": "updated title", "body": "updated body"})
    assert response.status_code == 200