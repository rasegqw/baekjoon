x = list(map(str, input().split('-')))

nums = []
for i in x:
    if i.find('+'):
        plus = list(map(int, i.split('+')))
        nums.append(sum(plus))
    else:
        nums.append(int(i))

result = nums[0]

for i in range(1, len(nums)):
    result -= nums[i]

print(result)