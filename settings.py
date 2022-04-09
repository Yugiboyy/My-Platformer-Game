

WIN_SIZE = (800, 600)
FPS = 30
TITLE = "PUNCH AND PUNCH"


GRID = []
GRID_SIZE = 64


for i in range(int(WIN_SIZE[0]/GRID_SIZE)+1):
    GRID.append([])
    for j in range(int(WIN_SIZE[1]/GRID_SIZE)+1):
        GRID[i].append([i*GRID_SIZE, j*GRID_SIZE])
print(len(GRID[0]),len(GRID[1]))
