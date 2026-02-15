# Простой пример
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# Сложный пример: матрица и обработка
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]  # List comprehension
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]