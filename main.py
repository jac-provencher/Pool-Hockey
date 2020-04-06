import pygame

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Circle:

    def __init__(self, color, radius, position):

        self.color = color
        self.radius = radius
        self.x, self.y = position
        self.velocity = 0

    def draw(self, surface):
        pass

class Surface:

    def __init__(self):
        pass

    def draw(self):
        pass

class Game:

    def __init__(self):

        self.surface = Surface()
        self.player1 = Circle(GREEN, 10, (10, 50))
        self.player2 = Circle(BLUE, 10, (200, 50))
        self.puck = Circle(RED, 5, (100, 50))

    def isGoal(self):
        pass

    def isCollision(self):
        pass

    def redraw(self):

        self.surface.draw()
        self.player1.draw()
        self.player2.draw()
        self.puck.draw()

    def mainloop(self):
        pass
