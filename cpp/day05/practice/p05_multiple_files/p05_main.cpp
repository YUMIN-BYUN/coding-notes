#include <iostream>
#include "p05_calculator.h"
#include "p05_info.h"

using namespace std;

int main()
{
    int a = 10;
    int b = 20;
    int c = 4;
    int d = 8;

    cout << a << " + " << b << " = " << add(a,b) << endl;
    cout << c << " * " << d << " = " << multiply(c,d) << endl;
    printInfo();

    return 0;
}