# Типы, try…except, работа с файлами и JSON

Краткое руководство по встроенным типам Python, обработке исключений, файловому вводу/выводу и работе с форматом JSON.

---

## 1. Типы данных

### Основные встроенные типы

| Тип | Пример | Описание |
|-----|--------|----------|
| `int` | `42` | Целое число |
| `float` | `3.14` | Число с плавающей точкой |
| `str` | `"hello"` | Строка |
| `bool` | `True` / `False` | Логическое значение |
| `list` | `[1, 2, 3]` | Изменяемый список |
| `tuple` | `(1, 2, 3)` | Неизменяемый кортеж |
| `dict` | `{"key": "value"}` | Словарь (ключ-значение) |
| `set` | `{1, 2, 3}` | Множество (уникальные элементы) |
| `NoneType` | `None` | Отсутствие значения |

### Проверка типа

```python
x = 42
print(type(x))        # <class 'int'>
print(isinstance(x, int))   # True
print(isinstance(x, (int, float)))  # True — проверка на несколько типов
```

### Приведение типов

```python
# str → int / float
age = int("25")
price = float("19.99")

# int / float → str
label = str(100)

# list ↔ set ↔ tuple
nums = [1, 2, 2, 3]
unique = set(nums)        # {1, 2, 3}
back = list(unique)       # [1, 2, 3]
fixed = tuple(back)       # (1, 2, 3)
```

### Изменяемые vs неизменяемые типы

| Изменяемые (mutable) | Неизменяемые (immutable) |
|----------------------|--------------------------|
| `list`, `dict`, `set` | `int`, `float`, `str`, `tuple`, `bool`, `NoneType` |

Неизменяемые объекты нельзя изменить после создания — при «изменении» создаётся новый объект.

---

## 2. try…except — обработка исключений

### Базовый синтаксис

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Деление на ноль!")
```

### Полная конструкция

```python
try:
    value = int(input("Введите число: "))
    result = 100 / value
except ValueError:
    print("Ошибка: нужно ввести целое число")
except ZeroDivisionError:
    print("Ошибка: нельзя делить на ноль")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
else:
    # выполняется, если исключений не было
    print(f"Результат: {result}")
finally:
    # выполняется всегда
    print("Блок выполнен")
```

### Распространённые исключения

| Исключение | Когда возникает |
|-----------|-----------------|
| `ValueError` | Неверное значение (напр. `int("abc")`) |
| `TypeError` | Несовместимые типы (`"a" + 1`) |
| `KeyError` | Несуществующий ключ словаря |
| `IndexError` | Выход за пределы списка |
| `FileNotFoundError` | Файл не найден |
| `ZeroDivisionError` | Деление на ноль |

### Вызов исключения вручную

```python
def get_positive(n):
    if n <= 0:
        raise ValueError(f"Число должно быть положительным, получено: {n}")
    return n
```

---

## 3. Работа с файлами

### Функция `open` — базовый подход

```python
# Открыть файл на чтение
file = open("data.txt", "r", encoding="utf-8")
content = file.read()
file.close()   # обязательно закрыть вручную
```

**Режимы открытия:**

| Режим | Описание |
|-------|----------|
| `"r"` | Чтение (файл должен существовать) |
| `"w"` | Запись (создаёт или перезаписывает) |
| `"a"` | Дозапись в конец файла |
| `"x"` | Создание нового файла (ошибка, если уже есть) |
| `"r+"` | Чтение и запись |
| `"b"` | Бинарный режим (добавляется к другим: `"rb"`, `"wb"`) |

### Контекстный менеджер `with` — рекомендуемый способ

`with` автоматически закрывает файл после выхода из блока, даже если возникло исключение.

```python
# Чтение всего файла
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Запись (перезапись) файла
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Привет, мир!\n")

# Дозапись в конец файла
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Новая строка\n")

# Чтение и перезапись (обновление)
with open("data.txt", "r+", encoding="utf-8") as file:
    content = file.read()
    file.seek(0)
    file.write(content.replace("мир", "Python"))
    file.truncate()
```

### Построчное чтение

```python
# Вариант 1 — итерация по файлу (эффективно для больших файлов)
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())   # strip() убирает \n в конце строки

# Вариант 2 — readlines() → список строк
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Вариант 3 — readline() → одна строка за раз
with open("data.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
```

### Создание нескольких файлов в цикле

```python
import os

os.makedirs("output", exist_ok=True)   # создать папку, если не существует

for i in range(1, 11):
    filename = f"output/file_{i}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Это файл номер {i}\n")

print("Создано 10 файлов в папке output/")
```

---

## 4. Модуль `os` — работа с файловой системой

```python
import os

# Текущая рабочая директория
print(os.getcwd())

# Список файлов и папок
print(os.listdir("."))

# Создать папку
os.makedirs("data/raw", exist_ok=True)

# Проверить существование
print(os.path.exists("data.txt"))     # True / False
print(os.path.isfile("data.txt"))     # только файл
print(os.path.isdir("output"))        # только папка

# Объединить пути (кроссплатформенно)
path = os.path.join("data", "raw", "file.txt")  # data/raw/file.txt

# Переименовать файл
os.rename("old_name.txt", "new_name.txt")

# Удалить файл
os.remove("file.txt")

# Удалить пустую папку
os.rmdir("empty_folder")

# Получить имя файла и расширение
name, ext = os.path.splitext("report.csv")  # ("report", ".csv")
```

---

## 5. Модуль `json` — работа с JSON

### `json.loads` и `json.dumps` — строки

```python
import json

# Строка JSON → объект Python
json_string = '{"name": "Alice", "age": 30, "active": true}'
data = json.loads(json_string)
print(data["name"])   # Alice

# Объект Python → строка JSON
user = {"name": "Bob", "scores": [9, 8, 10]}
json_string = json.dumps(user)                         # компактно
json_pretty = json.dumps(user, indent=2, ensure_ascii=False)  # форматированно
print(json_pretty)
```

### `json.load` и `json.dump` — файлы

```python
import json

# Чтение из файла
with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

# Запись в файл
with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, indent=2, ensure_ascii=False)
```

### Таблица функций

| Функция | Откуда/Куда | Описание |
|---------|-------------|----------|
| `json.loads(s)` | строка → Python | Парсит JSON-строку |
| `json.dumps(obj)` | Python → строка | Сериализует объект в JSON-строку |
| `json.load(f)` | файл → Python | Читает JSON из файлового объекта |
| `json.dump(obj, f)` | Python → файл | Записывает объект в файл как JSON |

---

## 6. Практические задачи

### Задача 1 — Средняя оценка продуктов

Файл `products.json`:

```json
[
  {"id": 1, "name": "Молоко", "rating": 4.5},
  {"id": 2, "name": "Хлеб", "rating": 3.8},
  {"id": 3, "name": "Сыр", "rating": 4.9},
  {"id": 4, "name": "Масло", "rating": 4.2}
]
```

Функция считывает список продуктов и выводит название каждого продукта вместе со средней оценкой всего каталога:

```python
import json


def show_products_with_avg_rating(filepath: str) -> None:
    with open(filepath, "r", encoding="utf-8") as file:
        products = json.load(file)

    if not products:
        print("Список продуктов пуст")
        return

    avg_rating = sum(p["rating"] for p in products) / len(products)

    print(f"{'Продукт':<20} {'Оценка':>7}")
    print("-" * 28)
    for product in products:
        print(f"{product['name']:<20} {product['rating']:>7.1f}")

    print("-" * 28)
    print(f"{'Средняя оценка:':<20} {avg_rating:>7.2f}")


show_products_with_avg_rating("products.json")
```

Пример вывода:
```
Продукт                Оценка
----------------------------
Молоко                    4.5
Хлеб                      3.8
Сыр                       4.9
Масло                     4.2
----------------------------
Средняя оценка:           4.35
```

---

### Задача 2 — Удаление продукта по названию

Функция считывает продукты, удаляет продукт с указанным названием и сохраняет обновлённый список обратно в файл:

```python
import json


def delete_product_by_name(filepath: str, name: str) -> None:
    with open(filepath, "r", encoding="utf-8") as file:
        products = json.load(file)

    original_count = len(products)
    products = [p for p in products if p["name"] != name]

    if len(products) == original_count:
        print(f"Продукт '{name}' не найден")
        return

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=2, ensure_ascii=False)

    print(f"Продукт '{name}' удалён. Осталось продуктов: {len(products)}")


delete_product_by_name("products.json", "Хлеб")
```

---

*Для деталей смотри документацию: [Built-in Types](https://docs.python.org/3/library/stdtypes.html), [Exceptions](https://docs.python.org/3/library/exceptions.html), [os](https://docs.python.org/3/library/os.html), [json](https://docs.python.org/3/library/json.html).*
