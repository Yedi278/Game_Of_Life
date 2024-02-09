#include <iostream>
#include "Board_lib.h"

int neighbors(board Board, int x, int y){   //Counts number of neighbors around i,j point
    int count = 0;

    for(int i=x-1; i<x+2; i++){
            for(int j=y-1; j<y+2; j++){

                if(i < 0 || i >= Board.rows) continue;
                if(j < 0 || j >= Board.cols) continue;
                if(Board.matrix[i][j]) count ++;

            }
    }

    if(Board.matrix[x][y]) return count-1;
    return count;
}

board play_turn(board Board){   //Makes one turn, it returns the board modified

    board tmp;

    for(int i=0; i<Board.rows; i++){
            for(int j=0; j<Board.cols; j++){

                int d = neighbors(Board, i,j);

                switch (Board.matrix[i][j])
                {
                case 1:

                    if(d == 2 || d == 3) tmp.matrix[i][j] = 1;
                    else tmp.matrix[i][j] =0;
                    break;

                case 0:

                    if(d == 3) tmp.matrix[i][j] = 1;
                    else tmp.matrix[i][j] = 0;
                    break;

                }
            }
    }
    return tmp;
}

