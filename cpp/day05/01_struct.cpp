#include <iostream>
#include <string>

using namespace std;

struct Student
{
    string name;
    int age;
    double gpa;
};

void printStudent(const Student& student)
{
    cout << "Name : " << student.name << endl;
    cout << "Age  : " << student.age << endl;
    cout << "GPA  : " << student.gpa << endl;
}

Student createStudent()
{
    Student student = {"Kim", 20, 4.25};
    return student;
}

int main()
{
    Student student1 = createStudent();

    printStudent(student1);

    Student students[3] =
    {
        {"Kim", 20, 4.25},
        {"Lee", 22, 3.90},
        {"Park", 19, 4.10}
    };

    cout << endl;
    cout << "Student List" << endl;

    for (int i = 0; i < 3; i++)
    {
        printStudent(students[i]);
        cout << endl;
    }

    return 0;
}