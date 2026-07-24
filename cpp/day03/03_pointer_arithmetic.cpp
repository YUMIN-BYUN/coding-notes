#include <iostream>

using namespace std;

int main()
{
    cout << "=== Size of Data Types ===" << endl;
    cout << "char   : " << sizeof(char) << " bytes" << endl;
    cout << "int    : " << sizeof(int) << " bytes" << endl;
    cout << "double : " << sizeof(double) << " bytes" << endl;

    cout << endl;

    char ch = 'A';
    int num = 10;
    double pi = 3.14;

    cout << "=== Size of Variables ===" << endl;
    cout << "ch  : " << sizeof(ch) << " bytes" << endl;
    cout << "num : " << sizeof(num) << " bytes" << endl;
    cout << "pi  : " << sizeof(pi) << " bytes" << endl;

    cout << endl;

    int numbers[5] = {10, 20, 30, 40, 50};

    cout << "=== Array Address ===" << endl;
    cout << "numbers      : " << numbers << endl;
    cout << "&numbers[0]  : " << &numbers[0] << endl;

    cout << endl;

    int* p = numbers;

    cout << "=== Pointer Arithmetic ===" << endl;
    cout << *p << endl;

    p++;
    cout << *p << endl;

    p += 2;
    cout << *p << endl;

    p--;

    cout << endl;

    cout << "=== Array Traversal using Pointer ===" << endl;

    for (int i = 0; i < 5; i++)
    {
        cout << *(numbers + i) << " ";
    }

    cout << endl;

    return 0;
}