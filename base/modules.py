# Импорт всего модуля
import math
print(math.sqrt(25))  # 5.0

# Импорт с псевдонимом (часто используется для pandas, numpy)
import pandas as pd
import numpy as np

# Импорт конкретных функций/классов из модуля
from collections import Counter, defaultdict
from math import pi, sin

# Импорт всего содержимого модуля (не рекомендуется, может быть конфликт имен)
# from os import *

# Создание собственного модуля
# 1. Создайте файл my_utils.py
# 2. Определите в нем функцию: def say_hello(name): return f"Hello, {name}"
# 3. В основном файле программы импортируйте его:
import my_utils
message = my_utils.say_hello("Alice")
print(message)

# Проверка на выполнение кода при запуске модуля напрямую
# В файле my_utils.py добавьте:
if __name__ == "__main__":
    # Этот код выполнится ТОЛЬКО если запустить my_utils.py напрямую
    print("Этот модуль запущен как основная программа")