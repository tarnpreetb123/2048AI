import pygame
import os
import sys
import math
from random import randint

xPath = os.path.join(sys.path[1], "Assets\X.png")
oPath = os.path.join(sys.path[1], "Assets\O.png")
blankPath = os.path.join(sys.path[1], "Assets\empty.jpg")

class GameBoard:

    def __init__(self, display):
        self.display = display
        self.rows = 4
        self.cols = 4
        self.width = 100
        self.height = 100
        self.board = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.score = 0
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.placeRandomTile()
        self.placeRandomTile()
        print(self.board)

    def draw(self):

        for i in range (self.rows):
            for j in range (self.cols):

                color = (255, 255, 255)
                textcolor = (0, 0, 0)

                if self.board[i][j] == 2:
                    textcolor = (244, 67, 54)
                elif self.board[i][j] == 4:
                    textcolor = (234, 30, 99)
                elif self.board[i][j] == 8:
                    textcolor = (156, 39, 176)
                elif self.board[i][j] == 16:
                    textcolor = (103, 58, 183)
                elif self.board[i][j] == 32:
                    textcolor = (33, 150, 243)
                elif self.board[i][j] == 64:
                    textcolor =  (0, 150, 136)
                elif self.board[i][j] == 128:
                    textcolor = (139, 195, 74)
                elif self.board[i][j] == 256:
                    textcolor = (60, 175, 80)
                elif self.board[i][j] == 512:
                    textcolor = (255, 152, 0)
                elif self.board[i][j] == 1024:
                    textcolor = (255, 87, 34)
                elif self.board[i][j] == 2048:
                    textcolor = (121, 85, 72)

                textsurface = self.myfont.render(str(self.board[i][j]), False, textcolor)
                self.display.blit(textsurface, (j * self.width, i * self.height, self.width, self.height))
                pygame.draw.rect(self.display, color, pygame.Rect(j * self.width, i * self.height, self.width, self.height))
                pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(j * self.width, i * self.height, self.width, self.height), 1)
                self.display.blit(textsurface, pygame.Rect(j * self.width, i * self.height, self.width, self.height))

        scorefont = pygame.font.SysFont("monospace", 50)

        label2 = scorefont.render("Score: " + str(self.score), 1, (0, 0, 0))
        self.display.blit(label2, (400, 20))

    def update(self, direction):
        returnValue = False

        if self.checkIfCanGo() == True:

            if direction != 0:

                rotations = self.getRotations(direction)

                for i in range(0, rotations):
                    self.rotateMatrixClockwise()

                if self.canMove():
                    self.moveTiles()
                    self.mergeTiles()
                    self.placeRandomTile()
                    returnValue = True

                for j in range(0, (4 - rotations) % 4):
                    self.rotateMatrixClockwise()
        return returnValue

    def placeRandomTile(self):
        count = 0
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.board[i][j] == 0:
                    count += 1

        i = math.floor(randint(0, 3))
        j = math.floor(randint(0, 3))

        while self.board[i][j] != 0:
            i = math.floor(randint(0, 3))
            j = math.floor(randint(0, 3))

        self.board[i][j] = 2

    def moveTiles(self):
        # We want to work column by column shifting up each element in turn.
        for i in range(0, self.rows):  # Work through our 4 columns.
            for j in range(0, self.cols - 1):  # Now consider shifting up each element by checking top 3 elements if 0.
                while self.board[i][j] == 0 and sum(self.board[i][
                                                    j:]) > 0:  # If any element is 0 and there is a number to shift we want to shift up elements below.
                    for k in range(j, self.cols - 1):  # Move up elements below.
                        self.board[i][k] =  self.board[i][k + 1]  # Move up each element one.
                    self.board[i][ self.rows - 1] = 0

    def mergeTiles(self):

        for i in range(0, self.rows):
            for k in range(0, self.rows - 1):
                if self.board[i][k] == self.board[i][k + 1] and self.board[i][k] != 0:
                    self.board[i][k] = self.board[i][k] * 2
                    self.board[i][k + 1] = 0
                    self.score += self.board[i][k]
                    self.moveTiles()

    def checkIfCanGo(self):
        for i in range(0, self.cols ** 2):
            if self.board[math.floor(i / self.rows)][i % self.rows] == 0:
                return True

        for i in range(0, self.rows):
            for j in range(0, self.cols - 1):
                if self.board[i][j] == self.board[i][j + 1]:
                    return True
                elif self.board[j][i] == self.board[j + 1][i]:
                    return True
        return False

    def canMove(self):
        for i in range(0, self.rows):
            for j in range(1, self.cols):
                if self.board[i][j - 1] == 0 and self.board[i][j] > 0:
                    return True
                elif (self.board[i][j - 1] == self.board[i][j]) and self.board[i][j - 1] != 0:
                    return True

        return False

    def rotateMatrixClockwise(self):
        for i in range(0, int(self.rows / 2)):
            for k in range(i, self.cols - i - 1):
                temp1 = self.board[i][k]
                temp2 = self.board[self.cols - 1 - k][i]
                temp3 = self.board[self.cols - 1 - i][self.cols - 1 - k]
                temp4 = self.board[k][self.cols - 1 - i]

                self.board[self.cols - 1 - k][i] = temp1
                self.board[self.cols - 1 - i][self.cols - 1 - k] = temp2
                self.board[k][self.cols - 1 - i] = temp3
                self.board[i][k] = temp4

    def isArrow(self):
        key = pygame.key.get_pressed()

        return (key[pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_LEFT] or key[pygame.K_RIGHT])

    def getRotations(self, direction):
        # key = pygame.key.get_pressed()
        #
        # if key[pygame.K_UP]:
        #     return 1
        # elif key[pygame.K_DOWN]:
        #     return 3
        # elif key[pygame.K_LEFT]:
        #     return 0
        # elif key[pygame.K_RIGHT]:
        #     return 2

        if direction == 1:
            return 1
        elif direction == 2:
            return 3
        elif direction == 3:
            return 0
        elif direction == 4:
            return 2

    def resetboard(self):
        self.board = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.score = 0
        self.placeRandomTile()
        self.placeRandomTile()

