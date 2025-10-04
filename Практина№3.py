def main():
    students = {}  # словник: ім'я -> оцінка

    print("Введіть ім'я студента та його оцінку (1-12). Для завершення введіть 'stop'.")

    while True:
        name = input("Ім'я студента: ")
        if name.lower() == "stop":
            break

        try:
            grade = int(input("Оцінка: "))
            if 1 <= grade <= 12:
                students[name] = grade
            else:
                print("❗ Оцінка має бути від 1 до 12.")
        except ValueError:
            print("❗ Введіть ціле число як оцінку!")

    if not students:
        print("Немає даних для аналізу.")
        return

    # Вивід усіх студентів
    print("\n📋 Список студентів та їх оцінки:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    # Обчислення середнього балу
    avg = sum(students.values()) / len(students)

    # Підрахунок категорій
    excellent = {n: g for n, g in students.items() if 10 <= g <= 12}
    good = {n: g for n, g in students.items() if 7 <= g <= 9}
    weak = {n: g for n, g in students.items() if 4 <= g <= 6}
    failed = {n: g for n, g in students.items() if 1 <= g <= 3}

    print("\n📊 Статистика:")
    print(f"Середній бал по групі: {avg:.2f}")
    print(f"Відмінники (10–12): {len(excellent)} → {', '.join(excellent.keys()) if excellent else 'немає'}")
    print(f"Хорошисти (7–9): {len(good)}")
    print(f"Відстаючі (4–6): {len(weak)}")
    print(f"Не здали (1–3): {len(failed)}")

if __name__ == "__main__":
    main()
