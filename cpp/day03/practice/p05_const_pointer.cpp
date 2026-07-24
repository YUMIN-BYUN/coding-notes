#include <iostream>

using namespace std;

int main()
{
    // Problem 1
    int a = 10;
    int b = 20;

    const int* p = &a;
    p = &b;

    cout << *p << endl;

    // Problem 2
    int value = 50;

    int* const q = &value;
    *q = 75;

    cout << value << endl;

    // Problem 3
    cout << endl;

    cout << "const int* p" << endl;
    cout << "--> Value: X, Pointer: O" << endl;

    cout << endl;

    cout << "int* const p" << endl;
    cout << "--> Value: O, Pointer: X" << endl;

    cout << endl;

    cout << "const int* const p" << endl;
    cout << "--> Value: X, Pointer: X" << endl;

    return 0;
}