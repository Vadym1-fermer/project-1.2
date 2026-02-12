class Lyudstvo:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print(f"{self.__name}, {self.__age} років")

    def speak(self):
        print("Людина говорить")


class Student(Lyudstvo):
    def __init__(self, name, age, uni):
        super().__init__(name, age)
        self.__uni = uni

    def info(self):  # поліморфізм
        super().info()
        print(f"Навчається в {self.__uni}")

    def speak(self):
        print("Студент відповідає на парі")


# використання
p = Lyudstvo("Іван", 30)
s = Student("Олег", 19, "ЛНУ")

p.info()
s.info()
s.speak()
