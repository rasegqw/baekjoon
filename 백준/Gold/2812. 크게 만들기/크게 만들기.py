import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num = input().strip()

stack = []
real_K = K

for i in range(N):

    while K!=0 and stack:
        if stack[-1] < num[i]:
            stack.pop()
            K-=1
            if K == 0 :
                break
        else:
            break
    
    stack.append(num[i])

# 남은 제거 횟수(K)가 있다면 스택 뒤쪽에서 K개를 제거
result = stack[:-K] if K else stack

print(''.join(result))
