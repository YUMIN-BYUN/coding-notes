#include <iostream>
#include <string>

using namespace std;

class Student
{
public:
    string name;

    static int studentCount;

    Student(string name)
    {
        this->name = name;
        studentCount++;
    }

    void showInfo()
    {
        cout << "Name: " << name << endl;
    }
};

int Student::studentCount = 0;

int main()
{
    Student s1("Alice");
    Student s2("Bob");
    Student s3("Charlie");

    s1.showInfo();
    s2.showInfo();
    s3.showInfo();

    cout << "Total Students: "
         << Student::studentCount << endl;

    return 0;
}