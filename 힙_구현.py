class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)                 # 끝에 삽입
        self._bubble_up(len(self.heap) - 1)   # 위로 올라가며 정렬

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)     # 루트 <-> 마지막 값 교환
        min_val = self.heap.pop()             # 마지막 값(원래 루트)을 꺼냄
        self._bubble_down(0)                  # 루트부터 아래로 정렬
        return min_val

    def peek(self):
        return self.heap[0] if self.heap else None

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _bubble_down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break
            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap)

h = MinHeap()
h.push(5)
h.push(3)
h.push(1)
h.push(10)
h.push(12)

print(h.pop())