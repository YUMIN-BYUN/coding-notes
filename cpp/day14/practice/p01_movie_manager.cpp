#include <iostream>

using namespace std;

void showMenu()
{
    cout << "==== Movie Manager ====" << endl;
    cout << "1. Add Movie" << endl;
    cout << "2. Show Movies" << endl;
    cout << "3. Find Movie" << endl;
    cout << "0. Exit" << endl;
    cout << "Select: ";
}

int main()
{
    int choice;

    while (true)
    {
        showMenu();
        cin >> choice;

        if (choice == 1)
        {
            cout << "Add Movie selected" << endl;
        }
        else if (choice == 2)
        {
            cout << "Show Movies selected" << endl;
        }
        else if (choice == 3)
        {
            cout << "Find Movie selected" << endl;
        }
        else if (choice == 0)
        {
            cout << "Program finished" << endl;
            break;
        }
        else
        {
            cout << "Invalid choice." << endl;
        }

        cout << endl;
    }

    return 0;
}