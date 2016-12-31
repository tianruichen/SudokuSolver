import random
import itertools
import math

class SudokuSolver:

    def __init__(self, grid):
        self.grid = grid
        self.newGrid = grid[:]
        self.possibleValues = {}
        self.empty = []
        self.remaining = 0
        self.initializeEmptySquares()
        self.solveSudoku()

    def initializeEmptySquares(self):
        rows = []
        for y in range(len(self.grid)):
            squares = []
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == 0:
                    self.possibleValues[(x,y)] = set()
                    squares.append((x,y))
                    self.remaining += 1
            rows.append(squares)
        self.empty = rows

    def getPossibleValues(self):
        possibleValues = {}
        for key in self.possibleValues.keys():
            possibleValues[key] = set()
        for key in self.possibleValues.keys():
            x, y = key
            for i in range(1, 10):
                if self.isPossibleValue(x, y, i):
                    possibleValues[key].add(i)
        return possibleValues

    def fillBestSquare(self):
        possibleValues = self.getPossibleValues()
        for key in possibleValues.keys():
            if self.newGrid[key[1]][key[0]] == 0 and len(possibleValues[key]) == 1:
                x, y = key
                self.newGrid[y][x] = list(possibleValues[key])[0]
                self.possibleValues.pop(key, None)
                self.remaining -= 1

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
        remaining = self.remaining
        while self.remaining > 0:
            self.fillBestSquare()
            if remaining == self.remaining:
                print "uh-oh"
                print self.getPossibleValues()
            remaining = self.remaining

