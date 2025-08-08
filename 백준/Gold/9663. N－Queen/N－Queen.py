import sys

N = int(sys.stdin.readline())

count = 0
cols = set()
A2 = set()
A1 = set()

def findP(row):
    global count

    if row == N:
        count += 1
        return
    
    for col in range(N):
        if col in cols or (row + col) in A1 or (row - col) in A2:
            continue

        cols.add(col)
        A2.add(row - col)
        A1.add(row + col)

        findP(row + 1)

        cols.remove(col)
        A2.remove(row - col)
        A1.remove(row + col)

findP(0)

print(count)