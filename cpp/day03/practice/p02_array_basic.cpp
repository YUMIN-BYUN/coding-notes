#include <iostream>

using namespace std;

int main()
{
    int numbers[5] = {1, 2, 3, 4, 5};

    numbers[2] = 30;
    numbers[4] = 50;
    for (int i = 0; i<=4; i++)
    {
        cout << numbers[i] << endl;
    }

    return 0;
}