def compress(x, y, size):
    current = video[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != current:
                half = size // 2
                return "(" + \
                    compress(x, y, half) + \
                    compress(x, y + half, half) + \
                    compress(x + half, y, half) + \
                    compress(x + half, y + half, half) + ")"
    return current

n = int(input())
video = [list(input().strip()) for _ in range(n)]
print(compress(0, 0, n))






