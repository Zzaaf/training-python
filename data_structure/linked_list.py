# Простой пример
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Создание списка
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Сложный пример: разворот списка
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Проверка
reversed_head = reverse_list(head)