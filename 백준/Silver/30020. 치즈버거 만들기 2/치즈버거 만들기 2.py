import sys

input = sys.stdin.readline

patty, cheese = map(int, input().split())

Burger_num = patty - cheese
if Burger_num <= 0 or Burger_num > cheese:
    print("NO")
else:
    print("YES")
    print(Burger_num)

    for _ in range(Burger_num-1):
        print("aba")
    
    rest_cheese = cheese - Burger_num + 1
    res = "aba"
    for _ in range(rest_cheese-1):
        res = res + "ba"

    print(res)