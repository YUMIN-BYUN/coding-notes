#include <iostream>

using namespace std;

void swapValues(int& x, int& y)
{
    int temp = x;
    x = y;
    y = temp;
}

int main()
{
    int first = 100;
    int second = 300;

    cout << "Before: " << first << " " << second << endl;

    swapValues(first, second);

    cout << "After: " << first << " " << second << endl;

    return 0;
}