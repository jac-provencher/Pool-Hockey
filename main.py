import pygame
import math

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def calculate_final_velocities(m1, v1_i, m2, v2_i):

    v1_f = ((m1 - m2)*v1_i + 2*m2*v2_i)/(m1 + m2)
    v2_f = ((m2 - m1)*v2_i + 2*m1*v1_i)/(m1 + m2)

    return v1_f, v2_f

class Circle:

    def __init__(self, color, radius, position):

        self.color = color
        self.radius = radius
        self.x, self.y = position
        self.velocity = 0

    def draw(self, surface):
        pass

class Window:

    def __init__(self):
        pass

    def draw(self):
        pass

class Game:

    def __init__(self):

        self.window = Window()
        self.player1 = Circle(GREEN, 10, (10, 50))
        self.player2 = Circle(BLUE, 10, (200, 50))
        self.puck = Circle(RED, 5, (100, 50))

    def isGoal(self):
        pass

    def isCollision(self):

        pos1 = (self.player1.x, self.player1.y)
        pos2 = (self.player2.x, self.player2.y)

        return math.dist(pos1, pos2) == self.player1.radius + self.player2.radius

    def redraw(self):

        self.window.draw()
        self.player1.draw(self.window)
        self.player2.draw(self.window)
        self.puck.draw(self.window)

    def mainloop(self):
        pass
