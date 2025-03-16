# import sys

# N = int(sys.stdin.readline())

# count = 0
# cols = set()
# A2 = set()      # 우하단 대각선
# A1 = set()      # 우상단 대각선

# def findP(row):
#     global count

#     if row == N:
#         count += 1
#         return
    
#     for col in range(N):
#         if col in cols or (row + col) in A1 or (row - col) in A2:
#             continue

#         cols.add(col)
#         A2.add(row - col)
#         A1.add(row + col)

#         findP(row + 1)

#         cols.remove(col)
#         A2.remove(row - col)
#         A1.remove(row + col)

# findP(0)

# print(count)
import sys

N = int(sys.stdin.readline())

count = 0
cols = set()
di_1 = set()  # 첫번째 대각선
di_2 = set()  # 두번째 대각선


def N_QUEEN(row):
    global count
    if row == N:
        count += 1
        return

    for col in range(N):
        if col in cols or (row - col) in di_1 or (row + col) in di_2:  # 같은 행에 있거나 같은 대각선에 있거나
            continue  # 스킵

        cols.add(col)
        di_1.add(row - col)
        di_2.add(row + col)

        N_QUEEN(row + 1)

        cols.remove(col)
        di_1.remove(row - col)
        di_2.remove(row + col)


N_QUEEN(0)

print(count)