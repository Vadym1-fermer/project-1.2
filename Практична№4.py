def format_price(price):
    return "ціна: " + str(round(price, 2)) + " грн"


def available_items(**items):
    return items


def make_order(available, prices):
    order = input("Введіть товари через кому: ").split(",")
    # прибираємо зайві пробіли без strip()
    cleaned_order = []
    for x in order:
        while x.startswith(" "):
            x = x[1:]
        while x.endswith(" "):
            x = x[:-1]
        cleaned_order.append(x)

    # перевірка наявності без all() і get()
    all_available = True
    for item in cleaned_order:
        if item not in available or available[item] != True:
            all_available = False
            break

    if all_available:
        total = 0
        for item in cleaned_order:
            total += prices[item]
        print("✅ Усі товари є. Загальна " + format_price(total))
    else:
        print("❌ Деякі товари відсутні!")


def main():
    prices = {"хліб": 25.5, "молоко": 42.0, "цукор": 38.75, "кава": 130.0, "яйця": 55.3}
    available = available_items(хліб=True, молоко=True, цукор=False, кава=True, яйця=True)

    while True:
        print("\n1. Ціни\n2. Купити\n3. Вихід")
        c = input("Ваш вибір: ")

        if c == "1":
            for k in prices:
                print(k + ": " + format_price(prices[k]))
        elif c == "2":
            make_order(available, prices)
        elif c == "3":
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()
