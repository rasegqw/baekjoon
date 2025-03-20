N = int(input())

count_def = 0
def count(n):
    global count_def

    if n == N and count_def !=0:
        return count_def
    
    left = n // 10
    right = n%10
    res = left + right
    a = right * 10 + res%10

    count_def += 1
    return count(a)

print(count(N))

