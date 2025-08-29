#include <iostream>
using namespace std;

int main() {
    
    int num1, num2, num3, rem;
    
    
    cout << "\nEnter the first number: ";
    cin >> num1;
     rem = num1 > 0;
     if (rem > 0 ){
     cout<< "The number is positive";
     }else{
         cout<< "The number is negative";
     }
     
    cout << "\nEnter the second number: ";
    cin >> num2;
    rem =  num2 > 0;
    if (rem > 0){
        cout<< "The number  is positive";
    }else{
        cout<< "The number is negative";
    }
    
    cout << "\nEnter a third number: ";
    cin >> num3;
    rem  = num3 > 0;
    if (rem > 0){
        cout<< "The number is positive";
    }else{
        cout<< "The number is negative";
    }

        return  0;
        }
