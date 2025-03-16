import sys

input = sys.stdin.readline
N = int(sys.stdin.readline())

City = [None] * N
cityNum=[]

for i in range(N):
    # City.append(a)
    City[i] = [i for i in list(map(int,input().split()))]


total = 0

def findM(N)