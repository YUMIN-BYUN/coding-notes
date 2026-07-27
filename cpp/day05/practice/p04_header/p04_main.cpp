#include <iostream>
#include "p04_math.h"
 
using namespace std;

int main()
{
    int a = 12;
    int b = 4;

    cout << a << " + " << b << " = " << add(a,b) << endl;
    cout << a << " - " << b << " = " << subtract(a,b) << endl;
    cout << a << " * " << b << " = " << multiply(a,b) << endl;

    return 0;
}