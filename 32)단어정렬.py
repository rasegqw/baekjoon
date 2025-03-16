N = int(input())

word=[]
for i in range(N):
    a = input()
    word.append(a)

word = sorted(set(word), key=lambda a: (len(a),  a.lower()))
for i in word:
    print(i)