#include <iostream>
#include <string>
#include <vector>
#include <utility>


using namespace std;

int main()
{
    vector<pair<string, int>> students;

    students.push_back(make_pair("Kim", 90));
    students.push_back(make_pair("Lee", 85));
    students.push_back(make_pair("Park", 100));

    for (const auto& student : students)
    {
        cout
            << student.first
            << " : "
            << student.second
            << endl;
    }
}