#include <iostream>

using namespace std;

int main()
{
    try
    {
        cout << "Try block started." << endl;

        throw 1;

        cout << "Try block finished." << endl;
    }
    catch (...)
    {
        cout << "Exception caught." << endl;
    }

    cout << "Program continues." << endl;

    return 0;
}