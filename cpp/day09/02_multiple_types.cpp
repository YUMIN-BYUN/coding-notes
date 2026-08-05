#include <iostream>

using namespace std;

template <typename T, typename U>
void show(T first, U second)
{
    cout << first << " " << second << endl;
}

int main()
{
    show(100, 3.14);
    show("Age", 20);

    return 0;
}