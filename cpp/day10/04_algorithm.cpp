#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> numbers =
    {
        30,10,50,20,40,20
    };

    sort(numbers.begin(), numbers.end());

    cout << "After sort : ";

    for (const auto& num : numbers)
    {
        cout << num << " ";
    }

    cout << endl;

    reverse(numbers.begin(), numbers.end());

    cout << "After reverse : ";

    for (const auto& num : numbers)
    {
        cout << num << " ";
    }

    cout << endl;

    auto it =
    find(
        numbers.begin(),
        numbers.end(),
        30
    );

    if (it != numbers.end())
    {
        cout << "30 Found" << endl;
    }

    cout
    << "Count of 20 : "
    << count(
        numbers.begin(),
        numbers.end(),
        20
    )
    << endl;

    cout
    << "Max : "
    << *max_element(
        numbers.begin(),
        numbers.end()
    )
    << endl;

    cout
    << "Min : "
    << *min_element(
        numbers.begin(),
        numbers.end()
    )
    << endl;

    return 0;
}