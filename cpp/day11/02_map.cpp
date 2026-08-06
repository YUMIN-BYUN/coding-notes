#include <iostream>
#include <map>

using namespace std;

int main()
{
    map<string, int> scores;

    scores["Alice"] = 95;
    scores["Bob"] = 87;
    scores["Chris"] = 100;

    cout << "Alice : " << scores["Alice"] << endl;
    cout << "Bob : " << scores["Bob"] << endl;

    cout << endl;

    for (const auto& student : scores)
    {
        cout << student.first << " : " << student.second << endl;
    }

    cout << endl;

    scores.erase("Bob");

    if (scores.find("Bob") == scores.end())
    {
        cout << "Bob not found" << endl;
    }

    return 0;
}