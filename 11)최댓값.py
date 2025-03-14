nums = []

for i in range(9):
    num = int(input())
    nums.append(num)

MAX = sorted(nums)[8]

def Find(a):
    for i in range(9):
        if nums[i] == a :
            return i

print(f"{MAX} {Find(MAX)+1}")