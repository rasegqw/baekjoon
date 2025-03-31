N = int(input())

a = input()
place = [0]

for i in a:
    place.append(int(i))

edge = [ [] for _ in range(N+1)]

for _ in range(N-1):
    A, B = map(int, input().split())

    edge[A].append(B)
    edge[B].append(A)    

cur = []
count = 0
for i in range(1, N+1):
    if place[i] == 0:
        continue
    cur.append(i)
    visited = []
    while cur:
        a = cur.pop()
        visited.append(a)
        for j in edge[a]:
            if j in visited:
                continue
            if place[j] == 1:
                count += 1
            else:
                cur.append(j)

print(count)