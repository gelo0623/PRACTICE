#include <iostream>
#include <ctime>
#include <cstdlib>
#include <string>
using namespace std;

int main () {
    
    int choose, again, select, num;
    char wah;
    
    string [ ] = 
     
    do{
        cout << "=====Guessing Game=====" << endl;
        cout << "1. Play Gambling" << endl;
        cout << "=======================" << endl;
        cout << "Select 1: ";
        cin >> select;
        
        num = (rand() % 10) + 1;
        do {
            
            cout << "\nSelect your guess: ";
            cin >> choose;
            
            if (choose < num){
                cout << "Too low";
            }
            else if (choose > num){
                cout << "Too high";
            }
        }
        while (choose != num);
        cout << "Congratulations" << endl;
        
        cout << "\nDo You Want To Try again: ";
        cin >> wah;
    }
    while (wah == 'y');
    
  
   return 0;
}
