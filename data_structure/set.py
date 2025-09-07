# Простой пример
primes = {2, 3, 5, 7}
primes.add(11)
print(primes)  # {2, 3, 5, 7, 11}

# Сложный пример: удаление дубликатов и операции с множествами
data = [1, 2, 2, 3, 4, 4, 5]
unique = set(data)
even = {x for x in unique if x % 2 == 0}  # Set comprehension
print(even)  # {2, 4}