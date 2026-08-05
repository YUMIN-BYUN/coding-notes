#include <iostream>

using namespace std;

void print(int x)
{
    cout << "Normal Function" << endl;
}

template <typename T>
void print(T x)
{
    cout << "Template Function" << endl;
}

int main()
{
    print(10);
    print(3.14);

    return 0;
}