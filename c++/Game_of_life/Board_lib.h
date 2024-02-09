#include <iostream>
#include <time.h>


class board{

    public:
        const int cols = 20;
        const int rows = 20;
        bool** matrix;

    board(){

        initialise();
        
        }

    void randomise(){
        srand((unsigned)time(NULL));

        for(int i=0; i<this->rows; i++){
            for(int j=0; j<this->cols; j++){
                matrix[i][j] = rand() % 2;
            }
        }
    }

    void initialise(){

        this->matrix = new bool*[rows];
        for (int i = 0; i < rows; ++i)
            matrix[i] = new bool[cols];
        
        for(int i=0; i<this->rows; i++){
            for(int j=0; j<this->cols; j++){

                matrix[i][j] = 0;
            }
        }
    }

    void clone(board Board){

        for(int i=0; i<Board.rows; i++){
            for(int j=0; j<Board.cols; j++){

                this->matrix[i][j] = Board.matrix[i][j];

            }
        }
    }

    void print_matrix(){

        for(int i=0; i<this->rows; i++){
            for(int j=0; j<this->cols; j++){

                std::cout << this->matrix[i][j] << ' ';
            }
            std::cout << '\n';
        }
    }


};