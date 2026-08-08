#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Student
{
public:
    string name;
    int score;

    Student(string name, int score)
    {
        this->name = name;
        this->score = score;
    }
};

int main()
{
    vector<Student> students;

    students.push_back(Student("Alice", 85));
    students.push_back(Student("Bob", 92));
    students.push_back(Student("Charlie", 78));
    students.push_back(Student("David", 95));

    auto it = find_if(
        students.begin(),
        students.end(),
        [](const Student& student)
        {
            return student.score >= 90;
        }
    );

    if (it != students.end())
    {
        cout << "First student above 90:" << endl;
        cout << "Name: " << it->name << endl;
        cout << "Score: " << it->score << endl;
    }

    int count = count_if(
        students.begin(),
        students.end(),
        [](const Student& student)
        {
            return student.score >= 90;
        }
    );

    cout << "Count: " << count << endl;

    return 0;
}