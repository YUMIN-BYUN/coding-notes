#include <iostream>

using namespace std;

template <typename T>
T multiply(T a, T b)
{
    return a * b;
}

int main()
{
    cout << multiply(3, 4) << endl;
    cout << multiply(2.5, 4.2) << endl;

    return 0;
}