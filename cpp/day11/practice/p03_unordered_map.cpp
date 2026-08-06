#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main()
{
    unordered_map<string, int> fruits;

    fruits["Apple"] = 1200;
    fruits["Banana"] = 800;
    fruits["Orange"] = 1500;
    fruits["Grape"] = 2000;

    for (auto const& fruit : fruits)
    {
        cout << fruit.first << " : "
             << fruit.second << endl;
    }

    cout << fruits["Orange"] << endl;

    fruits.erase("Banana");

    if (fruits.find("Banana") == fruits.end())
    {
        cout << "Banana deleted" << endl;
    }

    return 0;
}