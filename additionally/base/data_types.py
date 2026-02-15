# Объявление переменных разных типов
name = "Alice"                         # str (строка)
age = 30                               # int (целое число)
height = 1.75                          # float (число с плавающей точкой)
is_student = True                      # bool (логическое значение)
hobbies = ["reading", "hiking"]        # list (список)
coordinates = (50.45, 30.52)           # tuple (кортеж)
person = {"name": "Alice", "age": 30}  # dict (словарь)

# Проверка типов данных
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(is_student))  # <class 'bool'>

# Динамическая типизация: переменная может менять тип
value = 100
print(value, type(value))  # 100 <class 'int'>
value = "сто"
print(value, type(value))  # сто <class 'str'>