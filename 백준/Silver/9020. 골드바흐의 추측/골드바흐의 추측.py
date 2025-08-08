import math

def is_prime(x):
    if x == 2:
        return 2
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x%i ==0:
                return False
        return True

test_num = int(input())

for _ in range(0, test_num):
    x = int(input())
    small_num = int(x/2)
    while True:
        if is_prime(small_num) and is_prime(x-small_num):
            break
        else:
            small_num -= 1

    print(small_num, x-small_num)