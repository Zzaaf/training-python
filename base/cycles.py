# Цикл for для перебора элементов списка
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Я люблю {fruit}")

# Цикл for с функцией range()
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8 (start, stop, step)
    print(i)

# Цикл while с условием и оператором break
count = 0
while count < 5:
    print(count)
    count += 1
else:  # Выполняется, если цикл завершился нормально (не через break)
    print("Цикл завершен")

# Бесконечный цикл с прерыванием (часто используется в играх, серверах)
# while True:
#     user_input = input("Введите команду: ")
#     if user_input == "exit":
#         break