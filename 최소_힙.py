import sys
input = sys.stdin.readline

class HEAP:
    def __init__(self):
        self.heap = []

    def Push(self, value):
        self.heap.append(value)
        self._up(len(self.heap) -1)

    def Pop(self):
        if not self.heap:
            return 0
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        self._down(0)
        return val

    def Peek(self):
        return self.heap[0] if self.heap else None

    def _down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.heap[smallest] > self.heap[left]:
                smallest = left
            if right < n and self.heap[smallest] > self.heap[right]:
                smallest = right
            
            if smallest == index:
                break

            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            index = smallest

    def _up(self, index):
        while index>0:
            parent = (index - 1)//2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

N = int(input())
x = HEAP()

for i in range(N):
    a = int(input())
    if a == 0:
            print(x.Pop())

    else:
        x.Push(a)