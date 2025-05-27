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
import json

class Library:
    def __init__(self):
        self.books = []
        self.issued_books = {}
        self.issue_history = []  # список для статистики

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга "{book.title}" додана до бібліотеки.')

    def issue_book(self, title, person, date):
        book = self.find_book(title)
        if book and title not in self.issued_books:
            self.issued_books[title] = {"person": person, "date": date}
            self.issue_history.append({"title": title, "person": person, "issue_date": date, "return_date": None})
            print(f'Книга "{title}" видана {person} на дату {date}.')
        else:
            print(f'Книга "{title}" вже видана або відсутня.')

    def return_book(self, title, return_date):
        if title in self.issued_books:
            for record in self.issue_history:
                if record["title"] == title and record["return_date"] is None:
                    record["return_date"] = return_date
                    break
            del self.issued_books[title]
            print(f'Книга "{title}" повернена.')
        else:
            print(f'Книга "{title}" не була видана.')

    def get_statistics(self):
        total_issues = len(self.issue_history)
        returned = sum(1 for r in self.issue_history if r["return_date"] is not None)
        popular_books = {}
        total_days = 0
        count_days = 0

        for record in self.issue_history:
            title = record["title"]
            popular_books[title] = popular_books.get(title, 0) + 1
            if record["return_date"] is not None:
                days = record["return_date"] - record["issue_date"]
                total_days += days
                count_days += 1

        popular = max(popular_books, key=popular_books.get) if popular_books else "Немає даних"
        return_percent = (returned / total_issues * 100) if total_issues else 0
        avg_days = (total_days / count_days) if count_days else 0

        stats = {
            "Популярна книга": popular,
            "Відсоток повернення": f"{return_percent:.2f}%",
            "Середній час читання (у днях)": f"{avg_days:.2f}"
        }
        return stats

    def export_statistics_json(self):
        stats = self.get_statistics()
        with open("library_stats.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=4)
        print("Статистика збережена у файл library_stats.json")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# Приклад використання:
library = Library()
library.add_book(book1)

library.issue_book("Кобзар", "Іван", 10)
library.return_book("Кобзар", 40)

library.issue_book("Кобзар", "Марія", 50)
library.return_book("Кобзар", 70)

print("Статистика бібліотеки:", library.get_statistics())
library.export_statistics_json()
