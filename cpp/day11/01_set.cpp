#include <iostream>
#include <set>

using namespace std;

int main()
{
    set<int> numbers;

    numbers.insert(5);
    numbers.insert(2);
    numbers.insert(8);
    numbers.insert(2);
    numbers.insert(1);

    for (int num : numbers)
    {
        cout << num << " ";
    }

    cout << endl;

    cout << "Size: " << numbers.size() << endl;

    if (numbers.find(5) != numbers.end())
    {
        cout << "5 exists" << endl;
    }

    numbers.erase(2);

    for (int num : numbers)
    {
        cout << num << " ";
    }

    return 0;
}