import pygame
from pygame.locals import *

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == KEYDOWN and event.key == K_f:
                return 0

def title(screen):

    font_big = pygame.font.Font(pygame.font.get_default_font(), 36)
    font = pygame.font.Font(pygame.font.get_default_font(), 15)
    
    txt1 = font_big.render('Wellcome to the game of Life!', True, (255,255,255))
    txt2 = font.render('Press F to skip', True, (255,255,255))
    
    txt3 = font.render('Spacebar - Run/Stop || Mouse for putting new pieces', True, (255,255,255))
    txt4 = font.render('R - randomise grid', True, (255,255,255))
    
    screen.blit(txt1, dest=(50,300))
    screen.blit(txt2, dest=(50,350))
    pygame.display.flip()
    wait()

    screen.fill((0,0,0))
    screen.blit(txt3, dest=(50,300))
    screen.blit(txt4, dest=(50,350))

    pygame.display.flip()
    wait()
