#include <iostream>

using namespace std;

int main()
{
    int num;

    while (true)
    {
        cout << "Enter an integer: ";
        cin >> num;

        if (num == 0)
        {
            break;
        }

        if (num < 0)
        {
            continue;
        }

        cout << "You entered: " << num << endl;
    }

    cout << "Program terminated." << endl;

    return 0;
}