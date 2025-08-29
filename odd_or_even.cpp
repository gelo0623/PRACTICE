#include <iostream>
using namespace std;

int main() {
    
    int num1, num2, num3, rem;
    
    cout << "\nEnter the first number: ";
    cin >> num1;
     rem = num1 % 2;
     if (rem == 0){
     cout<< "The number is  even";
     }else{
         cout<< "The number is odd";
     }
     
    cout << "\nEnter the second number: ";
    cin >> num2;
    rem =  num2 % 2;
    if (rem ==  0){
        cout<< "The number  is even";
    }else{
        cout<< "The number is odd";
    }
    
    cout << "\nEnter a third number: ";
    cin >> num3;
    rem  = num3 % 2;
    if (rem == 0){
        cout<< "The number is even";
    }else{
        cout<< "The number is odd";
    }

        return  0;
        }
