def format_price(price):
    return "ціна: " + str(round(price, 2)) + " грн"


def make_order(available, prices):
    order = input("Введіть товари через кому: ").split(",")

    cleaned_order = []
    for x in order:
        while x.startswith(" "):
            x = x[1:]
        while x.endswith(" "):
            x = x[:-1]
        cleaned_order.append(x)

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


def run_menu(prices, available):
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