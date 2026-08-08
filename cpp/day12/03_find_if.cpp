#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> numbers = {10, 25, 30, 45, 50};

    auto it = find_if(
        numbers.begin(),
        numbers.end(),
        [](int n)
        {
            return n > 30;
        }
    );

    if (it != numbers.end())
    {
        cout << "Found: " << *it << endl;
    }
    else
    {
        cout << "Not found" << endl;
    }

    return 0;
}