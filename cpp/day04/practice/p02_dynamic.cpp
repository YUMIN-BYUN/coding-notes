#include <iostream>

using namespace std;

int main()
{
    int* ptr = new int;

    *ptr = 500;

    cout << *ptr << endl;

    delete ptr;

    ptr = nullptr;

    return 0;
}