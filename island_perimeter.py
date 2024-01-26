row = int(input("Enter row: "))
col = int(input("Enter collumn: "))

map_row = row + 2
map_col = col + 2

grid = []
map = [[0 for column in range(map_col)] for row in range(map_row)]

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    grid.append(a)

for i in range(1, map_row - 1):
    for j in range(1, map_col - 1):
        map[i][j] = grid[i-1][j-1]

print("MAP")
for i in range(row):
    for j in range(col):
        print(grid[i][j], end = " ")
    print()

def islandPerimeter(grid, row, col):
    perimeter = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                    cells = (grid[i-1][j], grid[i][j+1], grid[i+1][j], grid[i][j-1])
                    for cell in cells:
                        if cell == 0:
                            perimeter += 1
    return perimeter

print(f"Island perimeter is: {islandPerimeter(map, map_row, map_col)}")