#include <iostream>

using namespace std;

int main()
{
    int number;

    do
    {
        cout << "Enter a number (0 to exit): ";
        cin >> number;
    }
    while (number != 0);

    cout << "Program terminated." << endl;

    return 0;
}