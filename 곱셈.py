# from itertools import product

A, B, C = map(int, input().split())

# res = A%C
# for i in range(B):
#     res * res

def find(b):
    if b % 2 == 0:
        a = find(b//2) % C
        res = a * a
        return res%C
    elif b == 1 :
        return A%C
    else:
        a = find(b//2)%C
        res = a * ((a * A)%C)
        return res%C
    

print(find(B))
# for i in

# i = 0
# while A>=2**i :
#     i += 1

# A -= 2**(i-1)
# move = [i-1]
# if A != 0:        
#     for j in range(1, i):
#         if A >= 2**(i-j-1):
#             A -= 2**(i-j-1)
#             move.append(i-j-1)
#             if A == 0:
#                 break

# res = 0

# for c in product(range(len(move)), repeat=B):
#     total = sum(move[i] for i in c)
#     res += 1 << total



# print(res%C)
# namuji = []
# a = 0
# i = 0
# while i <= B//2 :
#     a = (A ** i)%C
#     namuji.append(a)
#     i += 1


# B - 2*i
