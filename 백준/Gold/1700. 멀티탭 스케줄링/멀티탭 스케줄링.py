N, K = map(int, input().split())
sequence = list(map(int, input().split()))

multitap = set()
ans = 0

for i in range(K):
    item = sequence[i]

    if item in multitap:
        continue  # 이미 꽂혀 있으면 패스

    if len(multitap) < N:
        multitap.add(item)  # 자리가 남으면 꽂기
        continue

    # 뽑아야 할 때
    # 현재 멀티탭에 있는 항목들의 "다음 사용 시점"을 본다
    latest_use = -1
    remove_item = -1

    for plugged in multitap:
        try:
            idx = sequence[i+1:].index(plugged)
        except ValueError:
            idx = float('inf')  # 다시 안 쓰임

        if idx > latest_use:
            latest_use = idx
            remove_item = plugged

    multitap.remove(remove_item)
    multitap.add(item)
    ans += 1

print(ans)
