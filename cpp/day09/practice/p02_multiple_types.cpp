#include <iostream>

using namespace std;

template <typename T, typename U>
void printPair(T first, U second)
{
    cout << first << " " << second << endl;
}

int main()
{
    printPair("Kim", 90);
    printPair(3.5, 'A');

    return 0;
}