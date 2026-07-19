from book import Book

library = [
    Book("Путь строителя", "Алексей Ковтунов"),
    Book("Имя нам Легион", "Дмитрий Дорничев и Евгений Лисицин"),
    Book("Антидемон", "Серж Винтеркей")
]

for book in library:
    print(f"{book.name} - {book.aftor}")