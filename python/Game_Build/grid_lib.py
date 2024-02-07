import numpy as np
import pygame

BLACK = 0,0,0
WHITE = 255,255,255

def grid(screen_size,density):
    shape = int(screen_size[0]/density),int(screen_size[1]/density)
    return np.zeros(shape,dtype=np.uint8)
    
def draw(surface, mat):

    surface_shape = surface.get_size()

    r = ( int(surface_shape[0]/mat.shape[0]),   int(surface_shape[1]/mat.shape[1]))
    contour = float(r[0])*0.1, float(r[1])*0.1

    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):

            if mat[i,j] == 1:
                rec = (r[0]*i, r[1]*j, r[0]-contour[0],r[1]-contour[1])
                c = np.random.randint(0,255,3)
                pygame.draw.rect(surface,c,rec)

def get_user_input(surface, mat, pos):
    surface_shape = surface.get_size()
    r = ( int(surface_shape[0]/mat.shape[0]),   int(surface_shape[1]/mat.shape[1]))

    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):

            if r[0]*i < pos[0] < r[0]*(i+1):
                if r[1]*j < pos[1] < r[1]*(j+1):
                    if mat[i,j] == 1: mat[i,j] = 0
                    elif mat[i,j] == 0: mat[i,j] = 1
