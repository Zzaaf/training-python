from queue import Queue

# Простой пример
q = Queue()
q.put("a")
q.put("b")
print(q.get())  # "a"

# Сложный пример: многопоточная обработка задач
import threading

def worker(q):
    while True:
        task = q.get()
        print(f"Processing {task}")
        q.task_done()

q = Queue()
for _ in range(3):
    threading.Thread(target=worker, args=(q,), daemon=True).start()

for task in ["task1", "task2", "task3"]:
    q.put(task)
q.join()  # Ожидание завершения всех задач