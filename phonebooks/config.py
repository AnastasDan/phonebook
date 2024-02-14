import csv

from .constants import FILENAME


def read_phonebook() -> list[list[str]]:
    """Читает телефонную книгу из файла."""
    phonebook: list[list[str]] = []

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                phonebook.append(row)

    except FileNotFoundError:
        create_empty_phonebook()
        print(f"Файл {FILENAME} создан.")

    return phonebook


def create_empty_phonebook() -> None:
    """Создает пустой файл телефонной книги."""
    with open(FILENAME, "w", encoding="utf-8"):
        pass


def save_phonebook(phonebook: list[list[str]]) -> None:
    """Сохраняет телефонную книгу в файл."""
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(phonebook)
