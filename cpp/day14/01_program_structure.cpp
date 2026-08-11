#include <iostream>

using namespace std;

void showMenu()
{
    cout << "===== Book Manager =====" << endl;
    cout << "1. Add Book" << endl;
    cout << "2. Show Books" << endl;
    cout << "3. Find Book" << endl;
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
            cout << "Add Book selected." << endl;
        }
        else if (choice == 2)
        {
            cout << "Show Books selected." << endl;
        }
        else if (choice == 3)
        {
            cout << "Find Book selected." << endl;
        }
        else if (choice == 0)
        {
            cout << "Program finished." << endl;
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