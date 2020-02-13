"""
Concerned with Storing and Retrieving Books from a json file.
"""

import json
import sqlite3

# SQLite Database
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE books (name VARCHAR(255), author VARCHAR(255), read BOOLEAN')
connection.commit()

connection.close()

# In memory database

books_file = 'books.json'

# Methods


def create_book_table():
    with open(books_file, 'w'):
        pass


def adding_books(name, author, read):
    name = name.title()
    author = author.title()
    read = read.title()

    if read == 'Yes':
        read = True
    elif read == 'No':
        read = False

    books = list_all()
    books.append({"name": name, "author": author, "read": False})
    _save_all(books)


def list_all():
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def edit_read(search):
    books = list_all()

    search = search.title()

    for book in books:
        if book['name'] == search and book['read'] == True:
            book['read'] = False
            print('You have not read this book.')
            print(book)
        elif book['name'] == search and book['read'] == False:
            book['read'] = True
            print('You have read this book.')
            print(book)

    _save_all(books)


def deleting_book(search):
    books = list_all()

    search = search.title()

    for book in books:
        if book['name'] == search:
            myindex = books.index(book)
            print(myindex)
            del books[myindex]

    _save_all(books)
