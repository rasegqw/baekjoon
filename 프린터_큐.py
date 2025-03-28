import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    count = 0
    nums, imp = map(int, input().strip().split())
    doc_list = deque(map(int, input().strip().split()))

    if nums == 1:
        print(1)
        continue
    else:
        j = 0
        while True:
            if doc_list[j] < max(doc_list):
                doc_list.rotate(-1)
                if imp == 0:
                    imp += len(doc_list)-1
                else:
                    imp -= 1
            else:
                doc_list.popleft()                    
                count += 1
                if imp == 0:
                    print(count)
                    break
                else:
                    imp -= 1