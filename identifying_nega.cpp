#include <iostream>
using namespace std;

int main() {
    
    int num1, num2, num3, num4, num5;
    
    cout<< "Enter a number: ";
    cin>> num1 >> num2 >> num3 >> num4 >> num5;
    
   int moly = num1 < 0;
       
       if (num2 < moly){
          moly = num2;
          cout<< "The negative number is: " << moly;
       }else if(num3 < moly){
           moly = num3;
           cout<< "The negative number is: " << moly;
       }else if(num4 < moly){
           moly = num4;
           cout<< "The negative number is: " << moly;
       }else if(num5 < moly){
           moly = num5;
           cout<< "The negative number is: " << moly;
       }else{
           cout<< "The negative number is: " << moly;
       }
       
       return 0;
   }
    
