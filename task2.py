class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Створюємо автора і книгу
author1 = Author("Тарас Шевченко")
book1 = Book("Кобзар", author1)
class Library:
    def __init__(self):
        self.books = []
        self.issued_books = {}  # словник: ключ - книга, значення - хто взяв і дата

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга "{book.title}" додана до бібліотеки.')

    def issue_book(self, title, person, date):
        book = self.find_book(title)
        if book and title not in self.issued_books:
            self.issued_books[title] = {"person": person, "date": date}
            print(f'Книга "{title}" видана {person} на дату {date}.')
        else:
            print(f'Книга "{title}" вже видана або відсутня.')

    def return_book(self, title, return_date):
        if title in self.issued_books:
            issue_date = self.issued_books[title]["date"]
            # Для простоти перевіримо, що повернення не пізніше 30 днів (не робимо справжній підрахунок дат)
            if return_date <= issue_date + 30:
                print(f'Книга "{title}" повернена вчасно.')
            else:
                print(f'Книга "{title}" повернена з запізненням.')
            del self.issued_books[title]
        else:
            print(f'Книга "{title}" не була видана.')

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# Приклад використання:
library = Library()
library.add_book(book1)
library.issue_book("Кобзар", "Іван", 10)  # 10 - уявна дата
library.return_book("Кобзар", 35)          # 35 - уявна дата повернення
