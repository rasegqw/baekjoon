import sys
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, x):
        self.value = x
        self.left = 0
        self.right = 0


def left_check(x, num):
    if x.left == 0:
        x.left = Node(num)
    elif x.left.value < num:
        right_check(x.left, num)
    else:
        left_check(x.left, num)

def right_check(x, num):
    if x.right == 0:
        x.right = Node(num)
    elif x.right.value < num:
        right_check(x.right, num)
    else:
        left_check(x.right, num)

def post_order(x):
    if x.left != 0:
        post_order(x.left)
    if x.right != 0:
        post_order(x.right)

    print(x.value)



biTree = None
while True:
    try:
        num = int(input())
        if biTree:
            if num < biTree.value:
                left_check(biTree, num)
            else:
                right_check(biTree, num)
        else:
            biTree = Node(num)

    except EOFError:
        break

post_order(biTree)

