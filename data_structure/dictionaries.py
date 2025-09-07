# Простой пример
person = {"name": "Alice", "age": 30}
person["city"] = "London"
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'London'}

# Сложный пример: вложенные словари и обработка
students = {
    "Alice": {"grades": [90, 85, 95], "age": 20},
    "Bob": {"grades": [80, 75, 70], "age": 21}
}

# Средняя оценка для каждого студента
avg_grades = {name: sum(data["grades"]) / len(data["grades"]) 
              for name, data in students.items()}
print(avg_grades)  # {'Alice': 90.0, 'Bob': 75.0}