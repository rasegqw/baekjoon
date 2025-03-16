N, r, c = map(int, input().split())

row_maxJisu =0
col_maxJisu =0

place = 0

def divide(maxJisu, row, col):
    global row_maxJisu, col_maxJisu, place
    if maxJisu == 1:
        if row == 0 and col == 0:
            return
        elif row == 1 and col == 0:
            place += 2
            return
        elif row == 0 and col == 1:
            place += 1
            return
        else:
            place += 3
            return


    for i in range(maxJisu):
        if row+1 <= 2**(i+1) :
            row_maxJisu = (i+1)
            break

    for i in range(maxJisu):
        if col+1 <= 2**(i+1) :
            col_maxJisu = i+1
            break
    
    if row_maxJisu == maxJisu and col_maxJisu == maxJisu:
        place += (2**(2*(maxJisu-1)))*3
        row -= 2**(row_maxJisu-1)
        col -= 2**(col_maxJisu-1)
        divide(maxJisu-1, row, col)
    
    elif row_maxJisu == maxJisu and col_maxJisu < maxJisu:
        place += (2**(2*(maxJisu-1)))*2
        row -= 2**(row_maxJisu-1)
        divide(maxJisu-1, row, col)

    elif row_maxJisu < maxJisu and col_maxJisu == maxJisu:
        place += (2**(2*(maxJisu-1)))*1
        col -= 2**(col_maxJisu-1)
        divide(maxJisu-1, row, col)
    else:
        divide(maxJisu-1, row, col)

divide(N, r, c)
print(place)