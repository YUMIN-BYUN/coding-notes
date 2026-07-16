#include <iostream>

using namespace std;

int main()
{
    int age;

    cout << "Enter your age: ";
    cin >> age;

    if (age >= 20)
    {
        cout << "Adult" << endl;
    }
    else
    {
        cout << "Minor" << endl;
    }

    return 0;
}