#include <iostream>
#include <string>

using namespace std;

int main()
{
    string name;
    int age;
    double height;

    cout << "Enter name: ";
    cin >> name;

    cout << "Enter age: ";
    cin >> age;

    cout << "Enter height: ";
    cin >> height;

    cout << endl;
    cout << "Name   : " << name << endl;
    cout << "Age    : " << age << endl;
    cout << "height : " << height << endl;

    return 0;
}