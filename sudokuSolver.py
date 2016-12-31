class SudokuSolver:

    def __init__(self, grid):
        self.grid = grid
        self.newGrid = grid[:]
        self.savedStates = []
        self.remaining = 0
        self.initializeConstraints()
        self.solveSudoku()
        self.valid = True

    def initializeConstraints(self):
        possibleValues = {}
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == 0:
                    possibleValues[(x,y)] = set()
                    for i in range(1, 10):
                        if self.isPossibleValue(x, y, i):
                            possibleValues[(x,y)].add(i)
                    self.remaining += 1
        self.savedStates.append(possibleValues)

    def getNewPossibleValues(self, possibleValues):
        newPossibleValues = {}
        for key in possibleValues.keys():
            newPossibleValues[key] = set()
            x, y = key
            for elem in list(possibleValues[key]):
                if self.isPossibleValue(x, y, elem):
                    newPossibleValues[key].add(elem)
        return newPossibleValues

    def isPossibleValue(self, x, y, value):
        for i in range(9):
            if i != x:
                if self.newGrid[y][i] == value:
                    return False
        for i in range(9):
            if i != y:
                if self.newGrid[i][x] == value:
                    return False
        sx = (x // 3) * 3
        sy = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if sx + i != x or sy + j != y:
                    if self.newGrid[sy + j][sx + i] == value:
                        return False
        return True

    def fillBestSquare(self):
        latestState = self.savedStates[-1]
        possibleValues = self.getNewPossibleValues(latestState)
        remaining = len(possibleValues.keys())
        backupLowest = 10
        backupKey = None
        reset = False
        for key in possibleValues.keys():    
            if self.newGrid[key[1]][key[0]] == 0 and len(possibleValues[key]) == 1:
                x, y = key
                self.newGrid[y][x] = list(possibleValues[key])[0]
                possibleValues.pop(key, None)
                self.remaining -= 1
                break
            elif len(possibleValues[key]) == 0:
                if len(self.savedStates) == 1:
                    return False
                else:
                    self.savedStates.pop()
                    latestState = self.savedStates[-1]
                    self.resetToState(latestState)
                    reset = True
                    break
            elif backupLowest > len(list(possibleValues[key])):
                backupLowest = len(list(possibleValues[key]))
                backupKey = key

        if not reset:
            if remaining == len(possibleValues.keys()):
                value = list(possibleValues[backupKey])[0]
                self.newGrid[backupKey[1]][backupKey[0]] = value
                self.remaining -= 1
                possibleValues[backupKey].remove(value)
                self.savedStates[-1] = possibleValues
                valueCopy = dict(possibleValues)
                valueCopy.pop(backupKey, None)
                self.savedStates.append(valueCopy)
            else:
                self.savedStates[-1] = possibleValues
        return True

    def resetToState(self, state):
        for key in state.keys():
            x, y = key
            if self.newGrid[y][x] != 0:
                self.newGrid[y][x] = 0
                self.remaining += 1


    def fullCheck(self):
        for y in range(9):
            for x in range(9):
                value = self.newGrid[y][x]
                if value == 0:
                    return False
                if not self.isPossibleValue(x,y,value):
                    return False
        return True

    def solveSudoku(self):
        while self.remaining > 0:
            validPuzzle = self.fillBestSquare()
            if not validPuzzle:
                self.valid = False
                break
    
    def getSolution(self):
        if not self.valid:
            return None
        return self.newGrid

