def format_price(price):
    return f"ціна: {price:.2f} грн"

def available_items(**items):
    return items

def make_order(available, prices):
    order = input("Введіть товари через кому: ").split(",")
    order = [x.strip() for x in order]
    if all(available.get(x, False) for x in order):
        total = sum(prices[x] for x in order)
        print(f"✅ Усі товари є. Загальна {format_price(total)}")
    else:
        print("❌ Деякі товари відсутні!")

prices = {"хліб": 25.5, "молоко": 42.0, "цукор": 38.75, "кава": 130.0, "яйця": 55.3}
available = available_items(хліб=True, молоко=True, цукор=False, кава=True, яйця=True)

while True:
    c = input("\n1. Ціни\n2. Купити\n3. Вихід\nВаш вибір: ")
    if c == "1":
        for k, v in prices.items(): print(f"{k}: {format_price(v)}")
    elif c == "2":
        make_order(available, prices)
    elif c == "3":
        break
    else:
        print("Невірний вибір.")
