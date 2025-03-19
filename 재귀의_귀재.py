import sys

T = int(input())

newstr = ''
strings = [''] * T
for i in range(T):
    strings[i] = sys.stdin.readline().strip()
count = 0

def recursion(string, left, right):
    global count
    count += 1
    if left>=right : return 1
    elif string[left] != string[right]: return 0
    else : return recursion(string, left+1, right-1)

def isPalindrm(string):
    return recursion(string, 0, len(string)-1)

for i in range(T):
    count = 0
    print(f'{isPalindrm(strings[i])} {count}')
