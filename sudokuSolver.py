import random
class SudokuSolver():

    def __init__(self, grid):
        self.grid = grid
        self.newGrid = grid[:]
        self.empty = []
        self.unused = []
        self.offset = []
        self.initializeEmptySquares()
        self.randomizeGrid()
        self.initializeErrors()

    def initializeEmptySquares(self):
        rows = []
        for y in range(len(grid)):
            squares = []
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    squares.append((x,y))
            rows.append(squares)
        self.empty = rows

    def randomizeGrid(self):
        for i in range(9):
            values = []
            for val in range(9):
                if val not in self.newGrid[i]:
                    values.append(val)
            self.unused.append(values[:])
            random.shuffle(values)
            for x, y in self.empty[i]:
                self.newGrid[y][x] = values.pop()

    def initializeErrors(self):
        for i in range(9):
            self.offset.append(self.checkRow(i))

    def checkNumber(self, x, y):
        conflicts = 0
        num = self.newGrid[y][x]
        for i in range(9):
            if i != y:
                if self.newGrid[y][i] == num:
                    conflicts += 1
                    break
        sx = (x // 3) * 3
        sy = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if sx + i != x or sy + j != y:
                    if self.newGrid[sy + j][sx + i] == num:
                        return conflicts + 1
        return conflicts

    def checkRow(self, y):
        totalOff = 0
        for i, j in self.empty[y]:
            totalOff += self.checkNumber(i, j)
        return totalOff

    def bestOffset(self, y):




    def solveSudoku(self):

    

def goalState()