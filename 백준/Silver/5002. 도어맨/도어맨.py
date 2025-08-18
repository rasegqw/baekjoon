import sys
input = sys.stdin.readline

memory_num = int(input())

lines = input()
cnt = 0

enter = ""
pending = ""

for M_W in lines:
    if not enter:
        enter = enter + M_W
        cnt += 1
    else:
        if M_W == "M":
            if pending == "W":
                cnt += 2
                pending = ""
            elif enter.find("W") != -1 and len(enter) <= memory_num:
                target = enter.find("W")
                after_remove = enter.split("W", 1)
                enter = ""
                enter = [enter + i for i in after_remove]
                enter = enter[-1]
                cnt += 1
            elif enter.find("W") == -1:
                if len(enter) < memory_num:
                    enter += M_W
                    cnt += 1
                elif len(enter) == memory_num and not pending:
                    pending = M_W
                else:
                    break
        if M_W == "W":
            if pending == "M":
                cnt += 2
                pending = ""
            elif enter.find("M") != -1 and len(enter) <= memory_num:
                target = enter.find("M")
                after_remove = enter.split("M", 1)
                enter = ""
                enter = [enter + i for i in after_remove]
                enter = enter[-1]
                cnt += 1
            elif enter.find("M") == -1:
                if len(enter) < memory_num:
                    enter += M_W
                    cnt += 1
                elif len(enter) == memory_num and not pending:
                    pending = M_W
                else:
                    break


print(cnt)