import pygame
import random

from enum import Enum
from collections import namedtuple


pygame.init()

class Direction(Enum):
    LEFT = 2
    RIGHT = 1
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x', 'y')

BLOCK_SIZE = 10

class SnakeGame:

    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, Point(self.head.x-BLOCK_SIZE, self.hear.y),
                      Point(self.head.x-2*BLOCK_SIZE, self.head.y)]


        self.score = 0
        self.food = None
        self._place_food()
        
        def place_food(self):
            x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
            y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE

            if self.food in self.snake:
                self._place_food()


        def play_step( )


    def play_step(self):
        pass





if __name__ == '__main__':
    game = SnakeGame()

    while True:
        game.play_step()





    pygame.quit()            