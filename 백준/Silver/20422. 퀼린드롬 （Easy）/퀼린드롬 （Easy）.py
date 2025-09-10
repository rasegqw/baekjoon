import sys

input = sys.stdin.readline

non_quil = ["C","F", "G", "J", "K", "c", "f", "g", "j", "k", "4", "6", "9"]

toUpper_quil = ["s","e","t","a","h","y","z"]
toLower_quil = ["B","D","R","L","N","P","Q"]

change_quil = ["E", "3", "S", "2", "Z", "5", "d", "b",
               "q", "p", "r", "7"]

flag = False

def solution(v):
    n = len(v)
    string2 = ""
    # print(v)
    for i in range(n-1, -1, -1):
        # print(v[i])
        if v[i] in change_quil:
            if v[i] == "E":
                string2 += "3"
            elif v[i] == "3":
                string2 += "E"
            elif v[i] == "S":
                string2 += "2"
            elif v[i] == "2":
                string2 += "S"
            elif v[i] == "Z":
                string2 += "5"
            elif v[i] == "5":
                string2 += "Z"
            elif v[i] == "d":
                string2 += "b"
            elif v[i] == "b":
                string2 += "d"
            elif v[i] == "q":
                string2 += "p"
            elif v[i] == "p":
                string2 += "q"
            elif v[i] == "r":
                string2 += "7"
            elif v[i] == "7":
                string2 += "r"
        else:
            string2 += v[i]
    # print(len(string2))
    # print(v)
    # print(string2)

    return string2


string = input().strip()
target = []

for i in string:
    if i in non_quil:
        print(-1)
        flag = True
        break
    elif i in toLower_quil:
        target.append(i.lower())
    elif i in toUpper_quil:
        target.append(i.upper())
    elif i not in change_quil:
        if i == "l" or i == "n":
            target.append(i)
        else:
            target.append(i.upper())
    else:
        target.append(i)

if not flag:
    string2 = solution(target)
    if string.upper() == string2.upper():
        print(string2)
    else: print(-1)
    
