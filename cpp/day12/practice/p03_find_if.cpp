#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> numbers = {3, 7, 12, 5, 18, 9};

    auto it = find_if(
        numbers.begin(),
        numbers.end(),
        [](int n)
        {
            return n % 2 == 0;
        }
    );

    if (it != numbers.end())
    {
        cout << "First even number: " << *it << endl;
    }

    else
    {
        cout << "No even number" << endl;
    }

    return 0;
}