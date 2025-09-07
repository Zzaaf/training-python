# Определение функции с параметром и возвратом значения
def greet(name, greeting="Hello"):  # Параметр с значением по умолчанию
    """Приветствует пользователя."""  # Строка документации (docstring)
    return f"{greeting}, {name}!"

message = greet("Bob", "Hi")
print(message)  # Hi, Bob!

# Функция с произвольным числом аргументов (*args, **kwargs)
def sum_all(*args):  # args - кортеж из всех переданных аргументов
    return sum(args)

result = sum_all(1, 2, 3, 4, 5)
print(result)  # 15

# Лямбда-функция (анонимная, для простых операций)
square = lambda x: x ** 2
print(square(5))  # 25

# Часто используется с sort/filter/map
numbers = [1, 5, 2, 8, 3]
sorted_numbers = sorted(numbers, key=lambda x: -x)  # Сортировка по убыванию
print(sorted_numbers)  # [8, 5, 3, 2, 1]