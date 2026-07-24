#include <iostream>

using namespace std;

int main()
{
    int x = 50;
    int y = 80;
    int* p = &x;
    *p = 100;
    p = &y;
    *p = 200;
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
}