# Базовый блок try-except
try:
    numerator = int(input("Введите числитель: "))
    denominator = int(input("Введите знаменатель: "))
    result = numerator / denominator
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except ValueError:
    print("Ошибка: Введите целые числа!")
except Exception as e:  # Общее исключение (ловит все, что не поймано выше)
    print(f"Произошла неизвестная ошибка: {e}")
else:
    print("Деление выполнено успешно!")  # Выполняется, если исключений не было
finally:
    print("Этот блок выполнится всегда.")  # Для закрытия ресурсов (файлов, сессий)

# Генерация собственных исключений
def validate_age(age):
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным!")
    elif age < 18:
        print("Вы еще молоды")
    else:
        print("Добро пожаловать")

try:
    validate_age(-5)
except ValueError as e:
    print(e)