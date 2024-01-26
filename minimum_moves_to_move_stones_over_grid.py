grid = []

for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input()))
    grid.append(a)

# for i in range(3):
#     for j in range(3):
#         print(grid[i][j], end = " ")
#     print()

for i in range(3):
    for j in range(3):
        if grid[i][j] > 1:
            for r in range