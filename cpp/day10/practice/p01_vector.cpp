#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> fruits;

    fruits.push_back("Apple");
    fruits.push_back("Banana");
    fruits.push_back("Orange");
    fruits.push_back("Grape");

    cout << fruits.size() << endl;

    for (int i = 0; i<fruits.size(); i++)
    {
        cout << fruits[i] << endl;
    }

    fruits.pop_back();
    cout << "After pop_back" << endl;

    for (int i = 0; i<fruits.size(); i++)
    {
        cout << fruits[i] << endl;
    }

    return 0;
}