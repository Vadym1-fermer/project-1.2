from decorator import timer_decorator
import time

@timer_decorator
def slow_function():
    print("Функція працює...")
    time.sleep(1.5)
    return "Готово!"

@timer_decorator
def sum_numbers(a, b):
    return a + b


# Виклики функцій
result1 = slow_function()
print(result1)

result2 = sum_numbers(5, 7)
print("Результат суми:", result2)
