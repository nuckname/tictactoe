# Main Method, not using methods
game_row_1 = [0, 0, 0]
game_row_2 = [0, 0, 0]
game_row_3 = [0, 0, 0]

display_row_1 = ["||", "||", "||"]
display_row_2 = ["||", "||", "||"]
display_row_3 = ["||", "||", "||"]

all_display_rows = [display_row_1, display_row_2, display_row_3]

print("Enter position of placement")
print("Row first then column")
print("[1,1] [1,2] [1,3]")
print("[2,1] [2,2] [2,3]")
print("[3,1] [3,2] [3,3]")
print("------------------------------")
running = True
turn = 'x'
while running == True:
    print(f"current turn {turn}")
    if turn == 'x':
        getRow = input("Enter row: ")
        getColumn = input("Enter column: ")
    elif turn == '0':
        getRow = input("Enter row: ")
        getColumn = input("Enter column: ")

    row = int(getRow)
    # - 1 because index starts at 0, and we use input for index
    column = int(getColumn) - 1

    game_all = [game_row_1, game_row_2, game_row_3]
    i = 0

    if row == 1:
        if game_row_1[column] == 0:
            if turn == 'x':
                game_row_1[column] = 1
            if turn == '0':
                game_row_1[column] = 2
            print(game_row_1)
        else:
            print("Square has been taken")
    elif row == 2:
        if game_row_2[column] == 0:
            if turn == 'x':
                game_row_2[column] = 1
            if turn == '0':
                game_row_2[column] = 2
            print(game_row_2)
        else:
            print("Square has been taken")
    elif row == 3:
        if game_row_3[column] == 0:
            if turn == 'x':
                game_row_3[column] = 1
            if turn == '0':
                game_row_3[column] = 2
            print(game_row_3)
        else:
            print("Square has been taken")

    z = 0
    x = 0
    while z <= 2:
        while x <= 2:
            if game_all[z][x] == 1:
                all_display_rows[z][x] = "x"
            if game_all[z][x] == 2:
                all_display_rows[z][x] = "O"
            x += 1
        z += 1
        x = 0

    print("")
    print("Current board: ")
    b = 0
    while b <= 2:
        print(all_display_rows[b])
        b += 1

    # checks for 3 in a row on cross
    in_a_row = 0
    column_counter = 0
    j = 0
    while j <= 2:
        if in_a_row == 3:
            print("3 across in a row! \nWin!")
            running = False
            break
        if game_all[j][column_counter] == 1:
            column_counter += 1
            in_a_row += 1
        else:
            j = j + 1
            column_counter = 0
            in_a_row = 0

    print("------------------------------")

    # checks for 3 in a row downwards
    row_counter = 0
    x = 0
    in_a_row = 0
    games_list_count = 0
    while x <= 2:
        if in_a_row == 3:
            print("3 down in a row! \nWin!")
            running = False
            break
        if game_all[games_list_count][row_counter] == 1:
            games_list_count += 1
            in_a_row += 1
        else:
            row_counter = 0
            in_a_row = 0
            x += 1

    #checks for 3 in a row diangle
    v = 0
    switch = 1
    while v <= 1:
        if game_row_1[0] == switch:
            if game_row_2[1] == switch:
                if game_row_3[2] == switch:
                    running = False
        if game_row_1[2] == switch:
            if game_row_2[1] == switch:
                if game_row_3[0] == switch:
                    running = False
        switch = 2
        v += 1
    #DRAW
    o = 0
    p = 0
    draw_count = 0
    while o <= 2:
        while p <= 2:
            if game_all[o][p] == 0:
                o = 3
                break
            else:
                draw_count += 1
                p += 1
        o += 1
        p = 0

    if draw_count == 9:
        print("DRAW!")
        running = False

    if turn == 'x':
        turn = '0'
    elif turn == '0':
        turn = 'x'
