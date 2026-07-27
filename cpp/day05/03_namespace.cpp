#include <iostream>
#include <string>

namespace School
{
    struct Student
    {
        std::string name;
        int age;
    };

    void printStudent(const Student& student)
    {
        std::cout << "Name : " << student.name << std::endl;
        std::cout << "Age  : " << student.age << std::endl;
    }
}

namespace Company
{
    struct Employee
    {
        std::string name;
        int id;
    };

    void printEmployee(const Employee& employee)
    {
        std::cout << "Name : " << employee.name << std::endl;
        std::cout << "ID   : " << employee.id << std::endl;
    }
}

int main()
{
    School::Student student = {"Kim", 20};
    Company::Employee employee = {"Lee", 1001};

    School::printStudent(student);

    std::cout << std::endl;

    Company::printEmployee(employee);

    return 0;
}