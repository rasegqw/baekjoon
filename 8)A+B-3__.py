x = int(input())

def add(ab):
    nums = ab.split(" ")
    a = int(nums[0])
    b = int(nums[1])
    return a+b

for i in range(x):
    A = input()
    print(f"{add(A)}")    
