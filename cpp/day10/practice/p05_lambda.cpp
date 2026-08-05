#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> numbers = {7,3,9,1,5};

    sort(
        numbers.begin(),
        numbers.end(),
        [](int a, int b)
        {
            return a > b;
        }
    );

    for (auto const& num : numbers)
    {
        cout << num << " ";
    }

    cout << endl;

    vector<string> words = {
        "Orange",
        "Fig",
        "Apple",
        "Watermelon"
    };

    sort(
        words.begin(),
        words.end(),
        [](const string& a, const string& b)
        {
            return a.size() > b.size();
        }
    );

    for (auto const& word : words)
    {
        cout << word << " ";
    }

    cout << endl;

    return 0;
}