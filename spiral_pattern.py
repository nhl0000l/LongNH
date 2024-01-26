size = int(input("Enter size number: "))

def spiralPattern(size):
    row = 0
    col = 0

    boundary = size - 1
    sizeLeft = size - 1
    flag = 1

    move = "r"

    matrix = [[0 for j in range(size)] for i in range(size)]

    for i in range(1, size * size + 1):
        matrix[row][col] = size * size + 1 - i

        if move == "r":
            col += 1
        elif move == "l":
            col -= 1
        elif move == "u":
            row -= 1
        elif move == "d":
            row += 1

        if i == boundary:
            boundary += sizeLeft

            if flag != 2:
                flag = 2
            else:
                flag = 1
                sizeLeft -= 1
            
            if move == "r":
                move = "d"
            elif move == "l":
                move = "u"
            elif move == "d":
                move = "l"
            elif move == "u":
                move = "r"        
        
    for i in range(size):
        for j in range(size):
            print(f"{matrix[i][j]:<2}", end=" ")
        print()

spiralPattern(size)