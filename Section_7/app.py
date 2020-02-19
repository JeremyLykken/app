from Section_7.utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

database.create_book_table()

def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            read_book()
        elif user_input == 'd':
            delete_book()
        else:
            print('Unknown command. Please try again.')
            user_input = input(USER_CHOICE)


# Add a new book to the database
def add_book():
    print('Let\'s add some books!')
    name = input('What is the book\'s title?: ')
    author = input('Who is the book\'s author?: ')
    read = input('Have you read this book?: ')
    database.adding_books(name, author, read)
    menu()


# List all books in the database
def list_books():
    print('Books currently in your library:')
    print(database.list_all())
    menu()


# Change read status for a title
def read_book():
    print('Let\'s change the status of a book.')
    search = input('What is the name of the book you want to change the status for?:')
    database.edit_read(search)
    menu()


# Delete a book from your library
def delete_book():
    print('Let\'s delete a book')
    search = input('What is the name of the book you want to remove?:')
    database.deleting_book(search)
    menu()


# Run program
menu()
print('The program has ended.')
