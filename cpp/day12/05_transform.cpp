#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> numbers = {1, 2, 3, 4, 5};
    vector<int> doubled(numbers.size());

    transform(
        numbers.begin(),
        numbers.end(),
        doubled.begin(),
        [](int n)
        {
            return n * 2;
        }
    );

    cout << "Original: ";

    for (int n : numbers)
    {
        cout << n << " ";
    }

    cout << endl;

    cout << "Doubled: ";

    for (int n : doubled)
    {
        cout << n << " ";
    }

    cout << endl;

    return 0;
}