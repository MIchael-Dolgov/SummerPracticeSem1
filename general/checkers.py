import re

def validate_and_format_phone_number(phone_number:str):
    """Регулярное выражение для проверки телефонного номера"""
    phone_pattern = re.compile(r'^\+?7[- ]?\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})$')
    
    match = phone_pattern.match(phone_number)
    if match:
        operator, first_part, second_part, third_part = match.groups()
        formatted_number = f'+7-({operator})-{first_part}-{second_part}-{third_part}'
        return formatted_number
    else:
        return None
    
def validate_capitalized_word(word: str):
    """Регулярное выражение для проверки и форматирования ФИО (Фамилия, Имя, Отчество)"""
    name_pattern_ru = re.compile(r'^[А-ЯЁ][а-яё]+$')
    name_pattern_en = re.compile(r'^[A-Z][a-z]+$')
    if name_pattern_ru.match(word) or name_pattern_en.match(word):
        return word
    else:
        return None
    
def validate_and_format_email(email: str):
    """Регулярное выражение для проверки email"""
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    
    match = email_pattern.match(email)
    if match:
        formatted_email = email
        return formatted_email
    else:
        return None

def validate_password(password: str):
    """Проверка пароля на соответствие требованиям безопасности."""
    if len(password) < 8:
        return None

    # Регулярные выражения для различных критериев
    have_uppercase = re.compile(r'[A-Z]')
    have_lowercase = re.compile(r'[a-z]')
    have_digit = re.compile(r'\d')
    have_special = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

    if (have_uppercase.search(password) and
        have_lowercase.search(password) and
        have_digit.search(password) and
        have_special.search(password)):
        return password
    else:
        return None
    