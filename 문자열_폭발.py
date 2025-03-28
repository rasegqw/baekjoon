Char_list = input().strip()

bomb = input().strip()
mini_b = bomb[-1]


while True:

    if bomb in Char_list:
        new_list = list(map(str, Char_list.split(bomb)))
        Char_list = ''.join(new_list)
    else:
        break
    

if Char_list:
    print(Char_list)
else:
    print('FRULA')