#include <iostream>

using namespace std;

int main()
{
    int true_password = 1234;
    int input_password = 0;
    
    while (input_password != true_password)
    {
        cout << "Enter password: ";
        cin >> input_password;

        if (input_password == true_password)
        {
            cout << "Access Granted";
            cout << endl;
        }
        else
        {
            cout << "Wrong Password";
            cout << endl;
            cout << endl;
        }
    }
    

    return 0;
    
}