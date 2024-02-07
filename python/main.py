import pygame
from grid_lib import*
from game import*

size = 600,600

pygame.init()
pygame.display.set_caption("~ Game Of Life ~")
screen = pygame.display.set_mode(size)

matrix = grid(size, density=4)
matrix = np.random.randint(0,2, size=matrix.shape)

run = True
while run:

    screen.fill(BLACK)
    draw(screen,matrix)
    matrix = game(matrix)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: run = False
        
    pygame.display.flip()
    pygame.time.delay(250)