N, K = map(int, input().split())

a = input()
stack = [None] * N

for i in range(len(a)):
    stack[i] = int(a[i])

start = 0

while len(stack) != N-K:
    if stack[start] > stack[start+1] :
        stack.pop(start+1)
    elif stack[start] < stack[start+1] :
        stack.pop(start)
    else:
        start += 2

ans =''
for i in stack:
    ans += str(i)

print(ans)

# while count != K:
#     max_index = stack.index(max(stack[start:N-K+count+1:1]))

#     for i in range(max_index):
#         stack.pop(i)
#         count += 1
    
#     start += 1