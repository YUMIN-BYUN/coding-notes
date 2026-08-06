#include <iostream>
#include <set>

using namespace std;

int main()
{
    set<int> numbers;
    numbers.insert(7);
    numbers.insert(4);
    numbers.insert(7);
    numbers.insert(2);
    numbers.insert(4);
    numbers.insert(9);

    for (auto const& num : numbers)
    {
        cout << num << " ";
    }

    cout << endl;

    return 0;
}