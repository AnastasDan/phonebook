from typing import Callable, Optional

from .config import save_phonebook
from .constants import PAGE_SIZE
from .utils import (
    calculate_total_pages,
    choose_field_to_edit,
    find_entry_by_phone_number,
    input_number,
    prompt_input,
)
from .validators import (
    validate_and_check_unique_phone_number,
    validate_name_surname,
    validate_organization,
    validate_patronymic,
)


def add_entry(phonebook: list[list[str]]) -> None:
    """
    Добавляет новую запись в телефонный справочник.
    """
    surname: str = prompt_input("Введите фамилию: ", validate_name_surname)
    name: str = prompt_input("Введите имя: ", validate_name_surname)
    patronymic: str = prompt_input(
        "Введите отчество (необязательно): ", validate_patronymic
    )
    company: str = prompt_input(
        "Введите название организации: ", validate_organization
    )
    work_phone: str = prompt_input(
        "Введите рабочий телефон: ",
        lambda x: validate_and_check_unique_phone_number(x, phonebook),
    )
    personal_phone: str = prompt_input(
        "Введите личный телефон: ",
        lambda x: validate_and_check_unique_phone_number(x, phonebook),
    )

    new_entry: list[str] = [
        surname,
        name,
        patronymic,
        company,
        work_phone,
        personal_phone,
    ]

    phonebook.append(new_entry)
    save_phonebook(phonebook)
    print("Запись добавлена.")


def edit_entry(phonebook: list[list[str]]) -> None:
    """
    Редактирует запись в телефонной книге по личному номеру телефона.
    """
    if not phonebook:
        print("Справочник пуст.")
        return

    phone_number_to_edit: str = input(
        "Введите личный телефон для поиска редактируемой записи: "
    )
    entry_number: Optional[int] = find_entry_by_phone_number(
        phonebook, phone_number_to_edit
    )

    if entry_number is None:
        print("Запись с данным номером телефона не найдена.")
        return

    while True:
        field: int = choose_field_to_edit()

        validation_funcs: dict[int, Callable[[str], bool]] = {
            1: validate_name_surname,
            2: validate_name_surname,
            3: validate_patronymic,
            4: validate_organization,
            5: lambda x: validate_and_check_unique_phone_number(x, phonebook),
            6: lambda x: validate_and_check_unique_phone_number(x, phonebook),
        }

        if 1 <= field <= 6:
            new_value: str = prompt_input(
                "Введите новое значение: ", validation_funcs[field]
            )
            phonebook[entry_number][field - 1] = new_value
            save_phonebook(phonebook)
            print("Запись обновлена.")

        elif field == 7:
            print("Редактирование завершено.")
            break

        else:
            print("Некорректный номер поля.")


def print_phonebook(phonebook: list[list[str]], page_size: int) -> None:
    """
    Выводит содержимое телефонного справочника постранично."""
    if len(phonebook) == 0:
        print("Справочник пуст.")
        return

    total_pages: int = calculate_total_pages(phonebook, PAGE_SIZE)
    print(f"Всего страниц в справочнике: {total_pages}")

    page: int = input_number("Введите номер страницы: ", 1, total_pages)
    start: int = (page - 1) * page_size
    end: int = min(start + page_size, len(phonebook))

    for index, row in enumerate(phonebook[start:end], start=1):
        record_number: int = index + (page - 1) * page_size
        print(f"{record_number}. {', '.join(row)}")


def search_entries(phonebook: list[list[str]]) -> None:
    """
    Выполняет поиск записей в телефонном справочнике по заданному запросу.
    """
    if len(phonebook) == 0:
        print("Справочник пуст.")
        return

    search_query: str = input("Введите поисковый запрос: ").lower()
    found_entries: bool = False

    for index, row in enumerate(phonebook, start=1):
        if any(search_query in entry.lower() for entry in row):
            print(f"{index}. {', '.join(row)}")
            found_entries = True

    if not found_entries:
        print("Записи не найдены.")
