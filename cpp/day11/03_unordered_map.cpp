#include <iostream>
#include <unordered_map>

using namespace std;

int main()
{
    unordered_map<string, int> scores;

    scores["Alice"] = 95;
    scores["Bob"] = 87;
    scores["Chris"] = 100;

    cout << "Alice : " << scores["Alice"] << endl;

    cout << endl;

    for (const auto& student : scores)
    {
        cout << student.first << " : "
             << student.second << endl;
    }

    cout << endl;

    if (scores.find("Bob") != scores.end())
    {
        cout << "Bob exists" << endl;
    }

    scores.erase("Bob");

    if (scores.find("Bob") == scores.end())
    {
        cout << "Bob deleted" << endl;
    }

    return 0;
}