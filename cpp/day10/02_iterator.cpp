#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> numbers = {10, 20, 30, 40, 50};

    cout << "Original elements: ";

    for (auto it = numbers.begin(); it != numbers.end(); it++)
    {
        cout << *it << " ";
    }

    cout << endl;

    for (auto it = numbers.begin(); it != numbers.end(); it++)
    {
        *it *= 2;
    }

    cout << "Modified elements: ";

    for (auto it = numbers.cbegin(); it != numbers.cend(); it++)
    {
        cout << *it << " ";
    }

    cout << endl;

    return 0;
}