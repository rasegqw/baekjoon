from queue import PriorityQueue
import sys

N = int(input())

q = PriorityQueue(maxsize=N)    

for i in range(N):
    q.put(int(sys.stdin.readline().strip()))
    # q.put(int(input()))

for i in range(N):
    print(q.get())




# def sort(n):
#     for i in range(len(n)-1, 0,-1):
#         if n[i] < n[i-1] :
#             n[i] , n[i-1] = n[i-1], n[i]
#         else:
#             break

# for i in range(N):
#     num.append(int(input()))
#     num.sort()