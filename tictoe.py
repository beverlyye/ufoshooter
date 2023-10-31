import pygame
import sys

class TicTacToe:
    def __init__(self):
        pygame.init()

        self.size = width, height = 640,320
        self.background = (224,241,244)
        self.color_game = (0, 55, 61)
        self.screen = pygame.display.set_mode(self.size)
        self.play_game()

def play_game(self):
    while True:
        self.screen.fill(self.background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()