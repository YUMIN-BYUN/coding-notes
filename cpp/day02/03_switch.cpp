#include <iostream>

using namespace std;

int main()
{
    int menu;

    cout << "1. Start" << endl;
    cout << "2. Settings" << endl;
    cout << "3. Exit" << endl;
    cout << "Select menu: ";
    cin >> menu;

    switch (menu)
    {
    case 1:
        cout << "Starting program..." << endl;
        break;

    case 2:
        cout << "Opening settings..." << endl;
        break;

    case 3:
        cout << "Exiting program..." << endl;
        break;

    default:
        cout << "Invalid menu." << endl;
    }

    return 0;
}