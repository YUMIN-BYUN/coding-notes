#include <iostream>
#include <string>

using namespace std;

class Student
{
public:
    string name;
    int age;
};

int main()
{
    Student s1;

    s1.name = "Alice";
    s1.age = 20;

    cout << "Name: " << s1.name << endl;
    cout << "Age: " << s1.age << endl;

    return 0;
}