# import math

# N = int(input())

# Jisu = int(math.log(N, 3))


# def truefalse(i, j, n):
#     if i in range(3**(n-1), 2*(3**(n-1))) and j in range(3**(n-1), 2*(3**(n-1))):
#         return False
#     if i == 0 or j == 0 :
#         return True
#     if n==1:
#         if i % 3 == 1 and j % 3 == 1:
#             return False
#         else:
#             return True
#     # elif i % 3 == 1 and j % 3 == 1:
#     #     return False
#     else:
#         if math.log(i,3) < n-1:
#             if math.log(j,3) < n-1:
#                 return truefalse(i, j, n-1)
#             elif (3**(n-1))<=j< 2*(3**(n-1)):
#                 return truefalse(i, j-3**(n-1), n-1)
#             else:
#                 return truefalse(i, j-2*(3**(n-1)), n-1)

#         elif (3**(n-1)) <= i < 2*(3**(n-1)):
#             if math.log(j,3) < n-1:
#                 return truefalse(i-3**(n-1), j, n-1)
#             elif (3**(n-1))<=j< 2*(3**(n-1)) :
#                 return truefalse(i-3**(n-1), j-3**(n-1), n-1)
#             else:
#                 return truefalse(i-3**(n-1), j-2*(3**(n-1)), n-1)

#         else:
#             if math.log(j,3) < n-1:
#             # if j in range(0, 3**(n-1)):
#             #     return truefalse(i-2*(3**(n-1)), j, n-1)
#                 return truefalse(i-2*(3**(n-1)), j, n-1)
#             elif (3**(n-1))<=j< 2*(3**(n-1)) :
#                 return truefalse(i-2*(3**(n-1)), j-3**(n-1), n-1)
#             else:
#                 return truefalse(i-2*(3**(n-1)), j-2*(3**(n-1)), n-1)
                
#             # elif j in range(3**(n-1), 2*(3**(n-1))):
#             #     return truefalse(i-3**(n-1), j-3**(n-1), n-1)
#             # else:
#             #     return truefalse(i-3**(n-1), j-2*(3**(n-1)), n-1)

# for j in range(N):          # 세로
#     for i in range(N):      # 가로        
#         if truefalse(i, j, Jisu):
#         # if i in range(3**(Jisu-1), 2*(3**(Jisu-1))) and j in range(3**(Jisu-1), 2*(3**(Jisu-1))):
#             print('*', end='')
#         else:
#             print(' ', end = '')
#     print('')


import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN//3) 
    L = []  
    
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))
