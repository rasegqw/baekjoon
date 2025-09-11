import sys

input = sys.stdin.readline

def solution(nums:list):

    if len(nums) <= 1:
        return nums, 0
    
    mid = len(nums) // 2
    left, lft_cnt = solution(nums[:mid])
    right, right_cnt = solution(nums[mid:])

    inv_cnt = lft_cnt + right_cnt
    merged = []
    i = j = 0

    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i+=1
            
        else:
            merged.append(right[j])
            j+=1
            inv_cnt += len(left) - i

    merged += left[i:]
    merged += right[j:]
    # print(inv_cnt)
    return merged, inv_cnt

if __name__=="__main__":
    n = int(input().strip())

    nums = list(map(int, input().split()))

    arr, ans = solution(nums)
    print(ans)