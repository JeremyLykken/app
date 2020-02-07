"""
Concerned with Storing and Retrieving Books from a list.
"""

# In memory database
books = [
    {
        'name': 'Sapiens', 'author': 'Yuval Harari', 'read': True
    },
    {
        'name': 'Blink', 'author': 'Malcolm Gladwell', 'read': False
    },
    {
        'name': 'Moby Dick', 'author': 'Herman Melville', 'read': False
    },
]


def adding_books(name, author, read):
    name = name.title()
    author = author.title()
    read = read.title()
    if read == 'Yes':
        read = True
    elif read == 'No':
        read = False
    books.append({'name': name, 'author': author, 'read': False})


def list_all():
    for book in books:
        print(book)


def edit_read(search):
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


def deleting_book(search):
    search = search.title()
    for book in books:
        if book['name'] == search:
            myindex = books.index(book)
            print(myindex)
            del books[myindex]
    print(books)
