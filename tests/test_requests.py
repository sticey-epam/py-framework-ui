import requests
import time
import pytest



def test_requests():

  headers = {
    "accept": "*/*",
    "Content-Type": "text/json; v=1.0" 
  }      

  request = requests.get('https://fakerestapi.azurewebsites.net')
  # assert request == "<Response [200]>"

  get_authors = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors') # Получение списка авторов
  get_author_one = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors/1') # Получение конкретного автора по его id

  print(get_author_one.json())

  add_book_params = {
    "id": 7777,
    "title": "Lord of the Rings",
    "description": "Fantasy Novel Written by J.R.R. Tolkien",
    "pageCount": 423,
    "excerpt": "Published July 29, 1954",
  }

  add_book = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Books', json=add_book_params, headers=headers) # Добавленне своєї книги
  print(add_book.json())

  add_user_params = {
    "id": 777,
    "username": "Sticey.uk",
    "password": "Lol_987"
  }

  add_user = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Users', json=add_user_params, headers=headers)
  print(add_user.json())

  update_book_params = {
    "id": 10,
    "title": "The Hobbit",
    "description": "Children Story",
    "pageCount": 350,
    "excerpt": "string",
    "publishDate": "2022-06-11T10:04:27.614Z"
  }

  update_book = requests.put(url='https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=update_book_params, headers=headers)
  print(update_book.json())


  delete_user = requests.delete(url='https://fakerestapi.azurewebsites.net/api/v1/Users/4')
  print(delete_user)