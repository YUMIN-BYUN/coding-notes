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
        cout << name << " joined." << endl;
    }

    ~Student()
    {
        cout << this->name << " left." << endl;
    }
};

int main()
{
    Student s1("Alice");
    Student s2("Bob");

    return 0;
}