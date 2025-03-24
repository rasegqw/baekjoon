from collections import deque

N, K = map(int, input().split())

result = []

people = deque(range(1, N+1))

while people:
    people.rotate(-K+1)
    result.append(people.popleft())

print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')

print(result[-1], end='>')