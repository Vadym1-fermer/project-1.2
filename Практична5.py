# lab5.py
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from faker import Faker
import pyjokes
from colorama import Fore, Style
import math
import emoji

# Використання 5 бібліотек у блоках try
print("=== Використання бібліотек ===")

# 1. requests — отримати сайт
try:
    response = requests.get("https://api.github.com")
    print("✅ requests:", response.status_code)
except Exception as e:
    print("❌ Помилка в requests:", e)

# 2. numpy — обчислення середнього значення
try:
    arr = np.array([10, 20, 30, 40])
    print("✅ numpy середнє:", np.mean(arr))
except Exception as e:
    print("❌ Помилка в numpy:", e)

# 3. pandas — створення DataFrame
try:
    df = pd.DataFrame({"Ім'я": ["Ана", "Богдан"], "Вік": [22, 25]})
    print("✅ pandas DataFrame:\n", df)
except Exception as e:
    print("❌ Помилка в pandas:", e)

# 4. faker — генерація фейкових даних
try:
    fake = Faker("uk_UA")
    print("✅ faker ім'я:", fake.name())
except Exception as e:
    print("❌ Помилка в faker:", e)

# 5. matplotlib — простий графік
try:
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.title("Простий графік")
    plt.savefig("graph.png")  # збереження у файл
    print("✅ matplotlib: графік збережено у graph.png")
except Exception as e:
    print("❌ Помилка в matplotlib:", e)
