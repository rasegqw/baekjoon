n = int(input())
nums = list(map(int, input().split()))

visited = [False] * n

max_res = 0
res = []


def result(arr):
    total = 0
    for i in range(n-1):
        total += abs(arr[i] - arr[i+1])
    return total

def backtrace():
    global res
    global max_res
    if len(res) == n:
        max_res = max(max_res, result(res))
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            res.append(nums[i])

            backtrace()

            visited[i] = False
            res.pop()

backtrace()
print(max_res)