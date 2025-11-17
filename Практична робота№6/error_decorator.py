def error_handler(error_code):
    """
    Декоратор, що перетворює виняток у спеціальний код помилки.
    error_code — це код, який повернеться при помилці.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return {
                    "error": True,
                    "error_code": error_code,
                    "message": str(e)
                }
        return wrapper
    return decorator
