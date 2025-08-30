#include <iostream>
using namespace std;

int main () {
    
    int purchase, total, discount, discounted_price;
    
    cout<< "Input purchase: ";
    cin>> purchase;
    
    total = 500;
    
    if (purchase >= 500) {
    discount = purchase * 0.10;         
    discounted_price = purchase - discount;
    }else {
    discounted_price = purchase;
    }
    cout << "Final price: " << discounted_price << endl;
    
    return 0;
}
