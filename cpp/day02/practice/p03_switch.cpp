#include <iostream>

using namespace std;

int main()
{
    int m;
    int n;
    int operation_num;

    cout << "Enter two integers: ";
    cin >> m >> n;

    cout << "1. Addition" << endl;
    cout << "2. Subtraction" << endl;
    cout << "3. Multiplication" << endl;
    cout << "4. Division" << endl;
    cout << "Select operation: ";
    cin >> operation_num;
    cout << endl;

    switch (operation_num)
    {
    case 1:
        cout << m + n << endl;
        break;
    
    case 2:
        cout << m - n << endl;
        break;

    case 3:
        cout << m * n << endl;
        break;

    case 4:
        if (n == 0)
        {
            cout << "Cannot divide by zero" << endl;
        }
        else 
        {
            cout << m / n << endl;
        }
        break;

    default:
        cout << "Invalid operation" << endl;
    }

    return 0;
}