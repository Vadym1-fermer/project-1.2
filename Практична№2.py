# Створюємо список з 10 int та 10 str
main_list = [12, 3, 45, 8, 22, 17, 5, 30, 1, 16,
             "banana", "apple", "pear", "grape", "kiwi",
             "orange", "melon", "peach", "plum", "cherry"]

# Розділяємо числа і рядки
ints = [x for x in main_list if isinstance(x, int)]
strs = [x for x in main_list if isinstance(x, str)]

# Сортуємо окремо
ints_sorted = sorted(ints)
strs_sorted = sorted(strs)

# Об’єднуємо (спочатку числа, потім строки)
sorted_list = ints_sorted + strs_sorted

# Знаходимо всі елементи, кратні двом
even_list = [x for x in ints_sorted if x % 2 == 0]

# Робимо окремий список строк у капсі
caps_list = [x.upper() for x in strs_sorted]

# Виводимо результати
print("Початковий список:", main_list)
print("Відсортований список (числа зростаюче + строки від А до Я):", sorted_list)
print("Список елементів кратних 2:", even_list)
print("Список строк у капсі:", caps_list)
