#include <iostream>
#include <string>

using namespace std;

class Person
{
public:
    string name;

    Person(string name)
    {
        this->name = name;
    }

    void introduce()
    {
        cout << "Name : " << name << endl;
    }
};

class Student : public Person
{
public:
    string major;

    Student(string name, string major)
        : Person(name)
    {
        this->major = major;
    }

    void showInfo()
    {
        introduce();
        cout << "Major : " << major << endl;
    }
};

int main()
{
    Student student("Alice", "Physics");

    student.showInfo();

    return 0;
}