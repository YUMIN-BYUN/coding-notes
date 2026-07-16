#include <iostream>

using namespace std;

int main()
{
    int age;

    cout << "Enter age: ";
    cin >> age;

    if (age >= 65)
    {
        cout << "Senior" << endl;
    }
    else if (age >= 20)
    {
        cout << "Adult" << endl;
    }
    else if (age >= 13)
    {
        cout << "Teen" << endl;
    }
    else 
    {
        cout << "Child" << endl;
    }
    
    return 0;
}