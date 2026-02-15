# Простой пример
coordinates = (10, 20)
x, y = coordinates  # Распаковка
print(x)  # 10

# Сложный пример: возврат нескольких значений из функции
def analyze_data(data):
    return min(data), max(data), sum(data) / len(data)

result = analyze_data([1, 2, 3, 4])
print(result)  # (1, 4, 2.5)