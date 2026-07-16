#include <iostream>

using namespace std;

int main()
{
    cout << "Using break:" << endl;

    for (int i = 1; i <= 10; i++)
    {
        if (i == 6)
        {
            break;
        }

        cout << i << " ";
    }

    cout << endl;
    cout << endl;

    cout << "Using continue:" << endl;

    for (int i = 1; i <= 10; i++)
    {
        if (i % 2 == 0)
        {
            continue;
        }

        cout << i << " ";
    }

    cout << endl;

    return 0;
}