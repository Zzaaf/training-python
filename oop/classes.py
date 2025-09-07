# Определение простого класса
class Dog:
    # Конструктор (инициализатор). self - ссылка на экземпляр класса.
    def __init__(self, name, breed, age=0):
        self.name = name        # Атрибут экземпляра
        self.breed = breed
        self.age = age

    # Метод экземпляра
    def bark(self):
        return f"{self.name} говорит: Гав!"

    # Еще один метод
    def have_birthday(self):
        self.age += 1
        return f"С днем рождения, {self.name}! Теперь ему {self.age} лет."

# Создание объектов (экземпляров класса)
dog1 = Dog("Бобик", "Дворняжка")
dog2 = Dog("Рекс", "Овчарка", 3)

print(dog1.name)         # Бобик
print(dog2.bark())       # Рекс говорит: Гав!
print(dog1.have_birthday()) # С днем рождения, Бобик! Теперь ему 1 год.

# Наследование
class GuardDog(Dog):  # Класс GuardDog наследуется от Dog
    def __init__(self, name, breed, age=0, is_on_duty=False):
        super().__init__(name, breed, age)  # Вызов конструктора родителя
        self.is_on_duty = is_on_duty        # Новый атрибут

    # Переопределение метода
    def bark(self):
        if self.is_on_duty:
            return f"{self.name} грозно лает: ВАФ-ВАФ!"
        else:
            return super().bark()  # Вызов метода родителя

guard_dog = GuardDog("Зевс", "Ротвейлер", 4, True)
print(guard_dog.bark())  # Зевс грозно лает: ВАФ-ВАФ!