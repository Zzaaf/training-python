# Простой пример
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

root = TreeNode("A")
root.children.append(TreeNode("B"))
root.children.append(TreeNode("C"))

# Сложный пример: обход в глубину (DFS)
def dfs(node):
    print(node.value)
    for child in node.children:
        dfs(child)

dfs(root)