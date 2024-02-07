import numpy as np

def init_board(matrix):

    matrix[3,3] = 1
    matrix[3,4] = 1
    matrix[4,4] = 1
    matrix[4,3] = 1

    matrix[6,5] = 1
    matrix[6,6] = 1
    matrix[6,7] = 1
    matrix[4,6] = 1

def neighbors(matrix, x,y):
    counter = 0

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i < 0 or j<0 or i>= matrix.shape[0] or j>= matrix.shape[1]: continue
            if matrix[i,j] == 1:
                counter += 1
                # print("True at ",x,y,"   ",i,j)
    if matrix[x,y] == 1: counter -= 1

    return counter

def game(mat1):

    mat2 = np.zeros(mat1.shape,dtype=np.uint8)
    
    for i in range(mat1.shape[0]):
        for j in range(mat1.shape[1]):

            d = neighbors(mat1, i,j)
            # if d !=0: print(i,j,d)

            if mat1[i,j] == 1:
                
                if  d == 2 or d ==3 : mat2[i,j] = 1
                else: mat2[i,j] = 0
            else:
                if d == 3: mat2[i,j] = 1
                else: mat2[i,j] = 0

    return mat2