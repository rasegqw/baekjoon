A, B, C = map(int, input().split())

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