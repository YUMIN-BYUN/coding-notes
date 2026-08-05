#include <iostream>
#include <vector>
#include <utility>
#include <string>

using namespace std;

int main()
{
    vector<pair<string, int>> students;

    students.push_back(make_pair("Alice", 95));
    students.push_back(make_pair("Bob", 87));
    students.push_back(make_pair("Charlie", 91));

    cout << "Student List" << endl;

    for (const auto& student : students)
    {
        cout
            << student.first
            << " : "
            << student.second
            << endl;
    }

    return 0;
}