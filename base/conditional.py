# Простая конструкция if-else
temperature = 25

if temperature > 30:
    print("Жарко")
elif 20 <= temperature <= 30:  # Проверка на вхождение в диапазон
    print("Тепло")
else:
    print("Прохладно")

# Использование логических операторов and, or, not
age = 18
has_license = True

if age >= 18 and has_license:
    print("Можно водить машину")
else:
    print("Нельзя водить машину")

# Сравнение строк (регистрозависимое)
user_input = "YES"
if user_input.lower() == "yes":  # Приводим к нижнему регистру для сравнения
    print("Пользователь согласен")