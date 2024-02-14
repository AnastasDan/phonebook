from phonebooks.config import read_phonebook
from phonebooks.constants import PAGE_SIZE
from phonebooks.phonebook_operations import (
    add_entry,
    edit_entry,
    print_phonebook,
    search_entries,
)
from phonebooks.utils import display_menu


def main() -> None:
    """
    Основная функция программы.
    Отвечает за интерактивное меню и обработку выбора пользователя.

    Пользователю предлагается выбрать одно из следующих действий:
    1. Показать телефонный справочник.
    2. Добавить новую запись.
    3. Редактировать существующую запись.
    4. Поиск записи по справочнику.
    0. Выход из программы.
    """
    phonebook = read_phonebook()
    while True:
        choice = display_menu()
        try:
            if choice in "1":
                print_phonebook(phonebook, PAGE_SIZE)
            elif choice == "2":
                add_entry(phonebook)
            elif choice == "3":
                edit_entry(phonebook)
            elif choice == "4":
                search_entries(phonebook)
            elif choice == "0":
                print("До встречи!")
                break
            else:
                print("Неправильный выбор. Пожалуйста, введите номер из меню.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


if __name__ == "__main__":
    main()
