from typing import Callable, Optional

from .exceptions import ValidationError


def display_menu() -> str:
    """
    Отображает главное меню программы.
    Запрашивает выбор пользователя.
    """
    menu: str = (
        "\nТелефонный справочник\n"
        "1. Показать справочник\n"
        "2. Добавить запись\n"
        "3. Редактировать запись\n"
        "4. Поиск\n"
        "0. Выйти\n"
    )

    return input(menu + "Выберите действие: ")


def choose_field_to_edit() -> int:
    """
    Отображает меню выбора поля для редактирования.
    Запрашивает выбор пользователя.
    """
    fields_menu: str = (
        "Доступные поля для редактирования:\n"
        "1. Фамилия\n"
        "2. Имя\n"
        "3. Отчество\n"
        "4. Название организации\n"
        "5. Рабочий телефон\n"
        "6. Личный телефон\n"
        "7. Завершить редактирование\n"
    )

    return int(input(fields_menu + "Выберите поле: "))


def calculate_total_pages(phonebook: list[list[str]], page_size: int) -> int:
    """
    Вычисляет общее количество страниц для отображения телефонной книги.
    """
    total_pages: int = (len(phonebook) + page_size - 1) // page_size

    return total_pages


def prompt_input(prompt: str, validation_func: Callable[[str], bool]) -> str:
    """
    Запрашивает у пользователя ввод и проводит его валидацию.
    """
    while True:
        try:
            value: str = input(prompt)
            validation_func(value)
            return value

        except ValidationError as error:
            print(f"{error}. Пожалуйста, попробуйте еще раз.")


def input_number(prompt: str, min_value: int, max_value: int) -> int:
    """
    Запрашивает у пользователя ввод числа.
    Проверяет его на соответствие заданным ограничениям.
    """
    while True:
        try:
            number: int = int(input(prompt))

            if (min_value is not None and number < min_value) or (
                max_value is not None and number > max_value
            ):
                print(f"Число должно быть от {min_value} до {max_value}.")

            else:
                return number

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


def standardize_phone_number(phone_number: str) -> str:
    """Приводит номер телефона к стандартному формату для проверки."""
    if phone_number.startswith("+"):
        phone_number = phone_number[1:]

    elif phone_number.startswith("8"):
        phone_number = "7" + phone_number[1:]

    return phone_number


def find_entry_by_phone_number(
    phonebook: list[list[str]], phone_number: str
) -> Optional[int]:
    """Находит запись по номеру телефона и возвращает её индекс."""
    for index, entry in enumerate(phonebook):
        if phone_number in entry[5]:
            return index

    return None
