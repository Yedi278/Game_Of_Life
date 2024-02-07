import pygame
from grid_lib import*
from game import*
from titlescreen import*
size = 600,600
speed = 200

pygame.init()
pygame.font.init()
pygame.display.set_caption("~ Game Of Life ~")
screen = pygame.display.set_mode(size)

matrix = grid(size, density=10)

title(screen)

# matrix = np.random.randint(0,2, size=matrix.shape)

run,start = True,False
while run:

    screen.fill(BLACK)
    
    draw(screen,matrix)
    
    if start == True:
        pygame.display.set_caption("~ Game Of Life (Running) ~")
        matrix = game(matrix)
    else:
        pygame.display.set_caption("~ Game Of Life (Pause) ~")

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if start: start = False
                else: start = True
            elif event.key == pygame.K_r:
                matrix = np.random.randint(0,2, size=matrix.shape)
            elif event.key == pygame.K_UP:
                speed += 10
            elif event.key == pygame.K_DOWN:
                speed -= 10
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            get_user_input(screen,matrix,pos)

    pygame.display.flip()
    pygame.time.delay(speed)