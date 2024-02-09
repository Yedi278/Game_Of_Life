#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include "game.h"
// #include <windows.h> 


int main(){

    board Board;
    Board.randomise();


    bool run = true;
    int count = 0;

    while(run){

        system("CLS");
        std::cout << "\nTurn " << count << '\n';
        Board.print_matrix();
        Board.clone(play_turn(Board));
        sleep(1);
        count++;
    }
    return 0;
}