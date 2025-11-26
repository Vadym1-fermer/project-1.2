# decorator.py

# Словник із кодами помилок
ERROR_CODES = {
    ValueError: "ERR001",
    TypeError: "ERR002",
    ZeroDivisionError: "ERR003",
    FileNotFoundError: "ERR004",
    Exception: "ERR999"  # Загальна помилка
}

def error_to_code(func):
    """
    Декоратор, який ловить винятки і повертає код помилки,
    замість аварійного завершення програми.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_type = type(e)
            code = ERROR_CODES.get(error_type, ERROR_CODES[Exception])
            return f"Помилка: {code} ({e})"
    return wrapper
