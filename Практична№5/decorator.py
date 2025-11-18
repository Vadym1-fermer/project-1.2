import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція: {func.__name__}")
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Час виконання: {end - start:.5f} секунд")
        return result

    return wrapper
