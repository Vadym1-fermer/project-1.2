# main.py

from decorator import error_to_code

@error_to_code
def divide(a, b):
    return a / b

@error_to_code
def get_list_element(lst, index):
    return lst[index]

@error_to_code
def convert_to_int(value):
    return int(value)

# Перевірка роботи
print(divide(10, 2))        # Все добре
print(divide(10, 0))        # ZeroDivisionError

print(get_list_element([1, 2, 3], 1))    # Все добре
print(get_list_element([1, 2, 3], 10))   # IndexError -> ERR999

print(convert_to_int("text"))  # ValueError -> ERR001
