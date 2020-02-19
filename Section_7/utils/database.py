"""
Concerned with Storing and Retrieving Books from a sqlite file.
"""

import sqlite3

# Methods


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name TEXT PRIMARY KEY, author TEXT, read BOOLEAN)')

    connection.commit()
    connection.close()


def adding_books(name, author, read):
    name = name.title()
    author = author.title()
    read = read.title()

    if read == 'Yes':
        read = True
    elif read == 'No':
        read = False

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (name, author, read))

    connection.commit()
    connection.close()


def list_all():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    for book in books:
        name = book[0]
        author = book[1]
        read = book[2]
        print(f"Name: {name}, Author: {author}, Read: {read}")

    connection.close()


def edit_read(search):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    search = search.title()

    cursor.execute('UPDATE books SET read=True WHERE name=?', (search,))

    connection.commit()
    connection.close()


def deleting_book(search):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    search = search.title()

    cursor.execute('DELETE FROM books WHERE name=?', (search,))

    connection.commit()
    connection.close()

