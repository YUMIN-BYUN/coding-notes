#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> numbers =
    {
        30,10,40,20,50
    };

    sort(
        numbers.begin(),
        numbers.end(),
        [](int a, int b)
        {
            return a > b;
        }
    );

    cout << "Descending : ";

    for (const auto& num : numbers)
    {
        cout << num << " ";
    }

    cout << endl;

    vector<string> words =
    {
        "Apple",
        "Kiwi",
        "Banana",
        "Pear"
    };

    sort(
        words.begin(),
        words.end(),
        [](const string& a,
           const string& b)
        {
            return a.size() < b.size();
        }
    );

    cout << "Length Sort : ";

    for (const auto& word : words)
    {
        cout << word << " ";
    }

    cout << endl;

    return 0;
}