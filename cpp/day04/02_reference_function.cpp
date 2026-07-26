#include <iostream>

using namespace std;

void change(int& value)
{
    value += 10;
}

void swapValues(int& a, int& b)
{
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    int num = 30;

    cout << "=== change() ===" << endl;
    cout << "Before: " << num << endl;

    change(num);

    cout << "After : " << num << endl << endl;

    int first = 100;
    int second = 300;

    cout << "=== swapValues() ===" << endl;
    cout << "Before: " << first << " " << second << endl;

    swapValues(first, second);

    cout << "After : " << first << " " << second << endl;

    return 0;
}