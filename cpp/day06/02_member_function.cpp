#include <iostream>
#include <string>

using namespace std;

class Student
{
public:
    string name;
    int age;

    void introduce()
    {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

int main()
{
    Student s1;

    s1.name = "Alice";
    s1.age = 20;

    s1.introduce();

    return 0;
}