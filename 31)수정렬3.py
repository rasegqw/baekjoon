from queue import PriorityQueue
import sys
import ctypes

N = int(input())

q = PriorityQueue(maxsize=N)    

for i in range(N):
    q.put((int(sys.stdin.readline().strip())))
    
for i in range(N):
    print(q.get())