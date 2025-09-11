import sys

TOGGLE = lambda x : x is False

input = sys.stdin.readline

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]


def toggle(board, y, x):
    for j in range(5):
        nx = x + dx[j]
        ny = y + dy[j]

        if 0 <= nx < 10 and 0<= ny < 10:
            board[ny][nx] = TOGGLE(board[ny][nx])

    return board

def solution(bit, check):

    board = [row[:] for row in check]
    cnt = 0

    for i in range(10):
        if (bit>>i) & 1 :
            board = toggle(board, 0, i)
            cnt += 1

    for i in range(1, 10):
        for j in range(10):
            if board[i-1][j]:
                toggle(board, i, j)
                cnt += 1

    # print(board)

    for i in range(10):
        if board[9][i]:
            return -1
        
    return cnt

if __name__=="__main__":
    
    check = []

    for _ in range(10):
        line = list(input().strip())
        check.append([target == "O" for target in line])

    ans = -1

    for bit in range(1<<10):
        res = solution(bit, check)
        if res != -1:
            if ans == -1 or res < ans:
                # print(res)
                ans = res
        
    print(ans)