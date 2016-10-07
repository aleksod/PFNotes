#def update_library(books, library):
#   '''
#   Input:  List - book names, Set - books already in library
#   Output: List - books that weren't in the library
#   '''
#   new_books = []
#   for book in books:
#       if book not in library:
#           print('The book, {} is new!'.format(book))
#           new_books.append(book)
#       library.add(book)
#   print library
#   return new_books

new_books = []

def update_library(books, library):
    for book in books:
        find_book(book, library)

def find_book(book, library):
    if book not in library:
        print("The book, %s is new!" % book)
        new_books.append(book)
    library.add(book)
