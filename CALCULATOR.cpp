#include <iostream>
using namespace std;

int main () {
    
    char choice, again;
    float add, subtract, multiply, divide, sum;
    int num1, num2;
    do {
        cout << "Press 'a' to add" << endl;
        cout << "Press 'b' to subtract" << endl;
        cout << "Press 'c' to multiply" << endl;
        cout << "Press 'b' to divide" << endl;
        cout << "Input your choice: ";
        cin >> choice;
        
        if(choice == 'a'){
            cout << "Input a number: ";
            cin >> num1;
            
            cout << "Input another number: ";
            cin >> num2;
            
            sum = num1 + num2;
            cout << "The sum is: " << sum;
        }
        else if (choice == 'b') {
            cout << "Input a number: ";
            cin >> num1;
            
            cout << "Input another number: ";
            cin >> num2;
            
            sum = num1 - num2;
            cout << "The sum is: " << sum;
        }
        else if (choice == 'c') {
            cout << "Input a number: ";
            cin >> num1;
            
            cout << "Input another number: ";
            cin >> num2;
            
            sum = num1 * num2;
            cout << "The sum is: " << sum;
        }
        else if (choice == 'd') {
            cout << "Input a number: ";
            cin >> num1;
            
            cout << "Input another number: ";
            cin >> num2;
            
            if (num2 == 0) {
                cout << "Undefined";
            }else {
                sum = num1 / num2;
                cout << "The sum is: " << sum;
            }
        }
        else if(choice == 'n'){
            cout << "exciting program" << endl;
            break;
            
        }else{
            cout << "Invalid choice" << endl;
        }
        
        cout << "\nDo you want to calculate again?: ";
        cin >> again;
        
    }
    while (again == 'y');
    
    cout << "Exciting program\n";
    return 0;
}
