N = int(input())

Anums = list(map(int, input().split()))

operator = list(map(int, input().split()))

max_result = int(-1e9)
min_result = int(1e9)

def calculate(index, result, add, sub, mul, div):
    global max_result, min_result

    if index == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    if add:
        calculate(index+1, result + Anums[index], add-1, sub, mul, div)
    if sub:
        calculate(index+1, result - Anums[index], add, sub-1, mul, div)
    if mul:
        calculate(index+1, result * Anums[index], add, sub, mul-1, div)
    if div:
        if result < 0:
            calculate(index+1, -(-result//Anums[index]), add, sub, mul, div-1)
        else:
            calculate(index+1, result//Anums[index], add, sub, mul, div-1)


calculate(1, Anums[0], operator[0],operator[1],operator[2],operator[3])


print(max_result)
print(min_result)