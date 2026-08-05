#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> numbers = {5,10,15,20,25};

    for (auto it = numbers.begin(); it != numbers.end(); it ++)
    {
        cout << *it << " ";
    }

    cout << endl;

    for (auto it = numbers.begin(); it != numbers.end(); it++)
    {
        *it += 3;
    }

    for (auto it = numbers.cbegin(); it != numbers.cend(); it ++)
    {
        cout << *it << " ";
    }

    cout << endl;
}