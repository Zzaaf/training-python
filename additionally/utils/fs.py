# Открытие файла для чтения (менеджер контекста 'with' автоматически закрывает файл)
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()  # Чтение всего файла в строку
    print(content)

# Построчное чтение больших файлов
with open("big_file.txt", "r") as file:
    for line in file:  # Читает по одной строке, экономя память
        print(line.strip())  # strip() убирает символы переноса

# Запись в файл
data_to_write = ["Строка 1\n", "Строка 2\n", "Строка 3\n"]
with open("output.txt", "w") as file:  # 'w' перезаписывает, 'a' - добавляет
    file.writelines(data_to_write)

# Работа с CSV-файлами (удобнее через модуль csv)
import csv
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(', '.join(row))