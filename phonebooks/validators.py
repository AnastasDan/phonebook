from .exceptions import ValidationError
from .utils import standardize_phone_number


def validate_and_check_unique_phone_number(
    phone_number: str, records: list[list[str]]
) -> bool:
    """Проверяет формат и уникальность номера среди списка контактов."""
    standardized_phone_number: str = standardize_phone_number(phone_number)

    if (
        not standardized_phone_number.isdigit()
        or not 10 <= len(standardized_phone_number) <= 15
    ):
        raise ValidationError(
            "Номер должен состоять из цифр и иметь длину от 10 до 15 цифр"
        )

    for contact in records:
        if standardized_phone_number in map(
            standardize_phone_number, contact[4:6]
        ):
            raise ValidationError("Номер должен быть уникальным")

    return True


def validate_name_surname(word: str) -> bool:
    """Проверяет, что имя и фамилия содержат только буквы и не пустые."""
    stripped_word: str = word.strip()

    if len(stripped_word) < 2 or not stripped_word.replace("-", "").isalpha():
        raise ValidationError(
            "Имя (фамилия) должно содержать только буквы и не быть пустым"
        )

    return True


def validate_patronymic(patronymic: str) -> bool:
    """Проверяет, что отчество содержит только буквы или пустое."""
    stripped_patronymic: str = patronymic.strip()

    if (
        stripped_patronymic
        and not stripped_patronymic.replace("-", "").isalpha()
    ):
        raise ValidationError(
            "Отчество должно содержать только буквы или быть пустым"
        )

    return True


def validate_organization(organization: str) -> bool:
    """Проверяет, что название организации не пустое."""
    if not organization.strip():
        raise ValidationError("Организация не должна быть пустой")

    return True
