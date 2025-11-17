from error_decorator import error_handler

@error_handler(error_code=1001)
def divide(a, b):
    return a / b

@error_handler(error_code=2002)
def get_item(lst, index):
    return lst[index]


result1 = divide(10, 0)
result2 = get_item([1, 2, 3], 5)
result3 = divide(10, 2)

print(result1)
print(result2)
print(result3)
