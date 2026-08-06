#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    map<string, int> students;
    students["Tom"] = 20;
    students["Jane"] = 22;
    students["Mike"] = 21;
    students["Lucy"] = 23;

    for (auto const& student : students)
    {
        cout << student.first << " : " << student.second << endl;
    }

    cout << students["Mike"] << endl;

    students.erase("Jane");

    if (students.find("Jane") == students.end())
    {
        cout << "Jane not found" << endl;
    }

    return 0;
}