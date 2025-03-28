class Node:
    def __init__(self, a):
        self.value = a
        self.left = None
        self.right = None

class BiTree:
    def __init__(self):
        self.nodes = {}

    def insert(self, val, L, R):
        if val not in self.nodes:
            self.nodes[val] = Node(val)

        if L != '.':
            self.nodes[L] = Node(L)
            self.nodes[val].left = self.nodes[L]

        if R != '.':
            self.nodes[R] = Node(R)
            self.nodes[val].right = self.nodes[R]

    def preorder(self, node):
        if node is None:
            return
        print(node.value, end="")  # 루트 출력
        self.preorder(node.left)   # 왼쪽 서브트리 탐색
        self.preorder(node.right)  # 오른쪽 서브트리 탐색

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)   # 왼쪽 서브트리 탐색
        print(node.value, end="") # 루트 출력
        self.inorder(node.right)  # 오른쪽 서브트리 탐색

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)   # 왼쪽 서브트리 탐색
        self.postorder(node.right)  # 오른쪽 서브트리 탐색
        print(node.value, end="")   # 루트 출력


N = int(input())

biTree = BiTree()

for _ in range(N):
    a = list(map(str, input().strip().split()))
    biTree.insert(a[0], a[1], a[2])

root = biTree.nodes["A"]  

biTree.preorder(root)
print()
biTree.inorder(root)
print()
biTree.postorder(root)
print()
# import sys

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.nodes = {}  # 노드를 저장할 딕셔너리

#     def insert(self, parent, left, right):
#         if parent not in self.nodes:
#             self.nodes[parent] = Node(parent)

#         if left != ".":
#             self.nodes[left] = Node(left)
#             self.nodes[parent].left = self.nodes[left]

#         if right != ".":
#             self.nodes[right] = Node(right)
#             self.nodes[parent].right = self.nodes[right]


# # 입력 처리
# input = sys.stdin.read
# data = input().split("\n")


