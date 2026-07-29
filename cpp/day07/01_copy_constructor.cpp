#include <iostream>
#include <string>

using namespace std;

class Student
{
public:
    string name;

    Student(string name)
    {
        this->name = name;
    }

    Student(const Student& other)
    {
        cout << "Copy Constructor Called" << endl;
        this->name = other.name;
    }

    void showInfo()
    {
        cout << "Name: " << name << endl;
    }
};

int main()
{
    Student s1("Kim");

    Student s2 = s1;

    s2.showInfo();

    return 0;
}