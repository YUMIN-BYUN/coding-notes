#include <iostream>

using namespace std;

int main()
{
    try
    {
        cout << "Start" << endl;
        throw 100;
        cout << "End" << endl;
    }

    catch(...)
    {
        cout << "Exception detected" << endl;
    }

    cout << "Program finished." << endl;
    
    return 0;
}