class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Author:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга "{book.title}" додана до бібліотеки.')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Книга "{title}" видалена з бібліотеки.')
                return
        print(f'Книга "{title}" не знайдена.')

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f'Знайдена книга: "{book.title}" автора {book.author.name}')
                return book
        print(f'Книга "{title}" не знайдена.')
        return None

# Приклад використання:
author1 = Author("Тарас Шевченко")
book1 = Book("Кобзар", author1)
library = Library()

library.add_book(book1)
library.find_book("Кобзар")
library.remove_book("Кобзар")
library.find_book("Кобзар")
