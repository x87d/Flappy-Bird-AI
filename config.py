import components
import pygame

win_height = 720
win_width = 550
window = pygame.display.set_mode((win_width, win_height))
background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, (win_width, win_height))
ground = components.Ground(win_width)
pipes = []