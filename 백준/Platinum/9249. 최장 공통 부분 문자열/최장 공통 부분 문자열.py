def build_suffix_array(s):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))

    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp[sa[0]] = 0

        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]]
            if (rank[sa[i]], rank[sa[i] + k] if sa[i] + k < n else -1) != \
               (rank[sa[i - 1]], rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1):
                tmp[sa[i]] += 1

        rank = tmp[:]
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1

    return sa

def build_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i

    h = 0
    lcp = [0] * n
    for i in range(n):
        if rank[i]:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h:
                h -= 1
    return lcp

# 입력
S1 = input().strip()
S2 = input().strip()
S = S1 + '$' + S2 + '#'

sa = build_suffix_array(S)
lcp = build_lcp(S, sa)

max_len = 0
pos = 0
len_S1 = len(S1)

for i in range(1, len(S)):
    a, b = sa[i - 1], sa[i]
    if (a < len_S1) != (b < len_S1):  # 다른 문자열에서 왔는지 확인
        if lcp[i] > max_len:
            max_len = lcp[i]
            pos = sa[i]

# 출력
print(max_len)
if max_len:
    print(S[pos:pos + max_len])
